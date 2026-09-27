"""
Unit tests for the Learning Path Recommendation System API.

Tests are organized into:
1. Model tests (no DB required)
2. Query sanitization tests (no DB required)
3. Algorithm unit tests (no DB required)
4. API endpoint validation tests (input validation, no DB required)
5. Health check tests (mocked DB)
"""
import json
from unittest.mock import patch

from django.test import TestCase

from models.user import User
from models.candidate import Candidate
from utilities.query_for_services import (
    _sanitize_string, query_create_user, query_register,
    query_get_id_by_email, query_search_lo, query_create_lo_has,
)


# ===================== MODEL TESTS =====================

class UserModelTest(TestCase):
    def test_create_user_from_dict(self):
        data = {'id': 1, 'name': 'Test', 'email': 'test@test.com', 'cost': 100, 'time': 50, 'career': None}
        user = User(data)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.cost, 100)
        self.assertEqual(user.time, 50)

    def test_user_none_cost_time(self):
        data = {'id': 1, 'name': 'Test', 'email': 'test@test.com', 'cost': None, 'time': None, 'career': None}
        user = User(data)
        self.assertEqual(user.cost, 0)
        self.assertEqual(user.time, 0)

    def test_is_time(self):
        user = User({'id': 1, 'name': 'T', 'email': 'e', 'cost': 0, 'time': 10, 'career': None})
        self.assertTrue(user.is_time())

    def test_is_cost(self):
        user = User({'id': 1, 'name': 'T', 'email': 'e', 'cost': 100, 'time': 0, 'career': None})
        self.assertTrue(user.is_cost())

    def test_is_time_false(self):
        user = User({'id': 1, 'name': 'T', 'email': 'e', 'cost': 0, 'time': 0, 'career': None})
        self.assertFalse(user.is_time())

    def test_get_user(self):
        data = {'id': 1, 'name': 'Test', 'email': 'test@test.com', 'cost': 100, 'time': 50, 'career': {'id': 5}}
        user = User(data)
        result = user.get_user()
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['career'], {'id': 5})


class CandidateModelTest(TestCase):
    def test_create_candidate(self):
        c = Candidate([1, 2, 3], lo=10)
        self.assertEqual(c.get_value(), [1, 2, 3])
        self.assertEqual(c.size, 3)
        self.assertEqual(c.get_lo_reference(), 10)

    def test_empty_candidate(self):
        c = Candidate()
        self.assertEqual(c.get_value(), [])
        self.assertEqual(c.size, 0)

    def test_extend_value(self):
        c = Candidate([1, 2], lo=5)
        c.extend_value([2, 3, 4])
        self.assertEqual(sorted(c.get_value()), [1, 2, 3, 4])

    def test_candidate_copies_input(self):
        original = [1, 2, 3]
        c = Candidate(original, lo=1)
        original.append(4)
        self.assertEqual(len(c.get_value()), 3)


# ===================== QUERY SANITIZATION TESTS =====================

class QuerySanitizationTest(TestCase):
    def test_sanitize_normal_string(self):
        self.assertEqual(_sanitize_string("hello"), "hello")

    def test_sanitize_injection_attempt(self):
        result = _sanitize_string("'; DROP DATABASE--")
        self.assertNotIn("'", result)
        self.assertNotIn(";", result)

    def test_sanitize_none(self):
        self.assertEqual(_sanitize_string(None), "")

    def test_sanitize_brackets(self):
        result = _sanitize_string("test{injection}[attack]")
        self.assertNotIn("{", result)
        self.assertNotIn("[", result)


class QueryBuilderTest(TestCase):
    def test_query_create_user(self):
        q = query_create_user(1, 100, 50)
        self.assertIn("id(u) = 1", q)
        self.assertIn("u.cost = 100", q)
        self.assertIn("u.time = 50", q)

    def test_query_register(self):
        q = query_register("Test User", "test@test.com")
        self.assertIn("Test User", q)
        self.assertIn("test@test.com", q)

    def test_query_get_id_by_email(self):
        q = query_get_id_by_email("test@test.com")
        self.assertIn("test@test.com", q)

    def test_query_create_user_rejects_string_id(self):
        with self.assertRaises(ValueError):
            query_create_user("abc", 100, 50)

    def test_query_search_lo_sanitizes(self):
        q = query_search_lo("python'; DROP")
        self.assertNotIn("';", q)

    def test_query_create_lo_has(self):
        q = query_create_lo_has(1, 5, 3, "knowledge")
        self.assertIn("HAS_KNOWLEDGE", q)
        self.assertIn("Level: 3", q)


# ===================== ALGORITHM TESTS =====================

class GeneticAlgorithmTest(TestCase):
    def test_crossover_does_not_modify_originals(self):
        from algorithm_v2.step2 import crossover
        ind1 = [1, 2, 3, 4]
        ind2 = [5, 6, 7, 8]
        ind1_copy = list(ind1)
        ind2_copy = list(ind2)
        crossover(ind1_copy, ind2_copy)
        self.assertEqual(ind1, [1, 2, 3, 4])
        self.assertEqual(ind2, [5, 6, 7, 8])

    def test_crossover_returns_two_children(self):
        from algorithm_v2.step2 import crossover
        result = crossover([1, 2, 3, 4], [5, 6, 7, 8])
        self.assertEqual(len(result), 2)

    def test_mutate_does_not_modify_original(self):
        from algorithm_v2.step2 import mutate
        ind = [1, 2, 3, 4]
        ind_copy = list(ind)
        mutate(ind_copy, [[10], [20], [30], [40]], 0)
        self.assertEqual(ind, [1, 2, 3, 4])

    def test_get_set_of_course_from_individual_flat(self):
        from algorithm_v2.step2 import get_set_of_course_from_individual
        result = get_set_of_course_from_individual([1, 2, 3])
        self.assertEqual(sorted(result), [1, 2, 3])

    def test_get_set_of_course_from_individual_nested(self):
        from algorithm_v2.step2 import get_set_of_course_from_individual
        result = get_set_of_course_from_individual([[1, 2], [3, 4]])
        self.assertEqual(sorted(result), [1, 2, 3, 4])

    def test_get_set_of_course_deduplicates(self):
        from algorithm_v2.step2 import get_set_of_course_from_individual
        result = get_set_of_course_from_individual([1, 1, 2, 2])
        self.assertEqual(sorted(result), [1, 2])


class Step3UtilityTest(TestCase):
    def test_are_lists_equal(self):
        from algorithm_v2.step3 import are_lists_equal
        self.assertTrue(are_lists_equal([1, 2, 3], [1, 2, 3]))
        self.assertFalse(are_lists_equal([1, 2, 3], [1, 2, 4]))
        self.assertFalse(are_lists_equal([1, 2], [1, 2, 3]))

    def test_is_common_node(self):
        from algorithm_v2.step3 import is_common_node_in_two_paths
        self.assertTrue(is_common_node_in_two_paths([1, 2, 3], [3, 4, 5]))
        self.assertFalse(is_common_node_in_two_paths([1, 2], [3, 4]))

    def test_is_in_path_final(self):
        from algorithm_v2.step3 import is_in_path_final
        self.assertTrue(is_in_path_final(3, [[1, 2, 3], [4, 5]]))
        self.assertFalse(is_in_path_final(6, [[1, 2, 3], [4, 5]]))


# ===================== API INPUT VALIDATION TESTS =====================

class IndexViewTest(TestCase):
    def test_index_returns_json(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'Learning Path Recommendation System API')
        self.assertEqual(data['status'], 'running')


class UserApiValidationTest(TestCase):
    def test_login_missing_email(self):
        response = self.client.get('/apis/user/login')
        self.assertEqual(response.status_code, 400)

    def test_register_missing_body(self):
        response = self.client.post('/apis/user/register', content_type='application/json', data='{}')
        self.assertEqual(response.status_code, 400)

    def test_create_user_missing_id(self):
        response = self.client.post('/apis/user/create',
                                     content_type='application/json',
                                     data=json.dumps({'cost': 100, 'time': 50}))
        self.assertEqual(response.status_code, 400)

    def test_objective_missing_fields(self):
        response = self.client.post('/apis/user/objective',
                                     content_type='application/json',
                                     data=json.dumps({'user_id': 1}))
        self.assertEqual(response.status_code, 400)

    def test_get_user_info_missing_id(self):
        response = self.client.get('/apis/user/info/')
        self.assertEqual(response.status_code, 400)

    def test_get_user_info_invalid_id(self):
        response = self.client.get('/apis/user/info/?id=abc')
        self.assertEqual(response.status_code, 400)

    def test_get_lo_need_missing_id(self):
        response = self.client.get('/apis/user/need')
        self.assertEqual(response.status_code, 400)

    def test_learning_path_missing_id(self):
        response = self.client.get('/apis/user/learning-path')
        self.assertEqual(response.status_code, 400)


class CareerApiValidationTest(TestCase):
    def test_career_by_id_missing(self):
        response = self.client.get('/apis/career/one')
        self.assertEqual(response.status_code, 400)

    def test_career_by_id_invalid(self):
        response = self.client.get('/apis/career/one?id=abc')
        self.assertEqual(response.status_code, 400)

    def test_career_lo_need_missing_id(self):
        response = self.client.get('/apis/career/lo')
        self.assertEqual(response.status_code, 400)


class CourseApiValidationTest(TestCase):
    def test_course_info_missing_id(self):
        response = self.client.get('/apis/course')
        self.assertEqual(response.status_code, 400)

    def test_course_provided_lo_missing(self):
        response = self.client.get('/apis/course/provided/lo')
        self.assertEqual(response.status_code, 400)

    def test_course_required_lo_missing(self):
        response = self.client.get('/apis/course/required/lo')
        self.assertEqual(response.status_code, 400)


class LOApiValidationTest(TestCase):
    def test_user_has_get_missing_id(self):
        response = self.client.get('/apis/user/has')
        self.assertEqual(response.status_code, 400)

    def test_user_has_delete_missing_body(self):
        response = self.client.post('/apis/user/has/delete',
                                     content_type='application/json', data='{}')
        self.assertEqual(response.status_code, 400)

    def test_user_has_create_missing_body(self):
        response = self.client.post('/apis/user/has/create',
                                     content_type='application/json', data='{}')
        self.assertEqual(response.status_code, 400)


# ===================== HEALTH CHECK TESTS =====================

class HealthCheckTest(TestCase):
    @patch('apis.common_apis.check_connection')
    def test_health_check_connected(self, mock_check):
        mock_check.return_value = {"status": "connected", "message": "OK"}
        response = self.client.get('/apis/health/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'healthy')

    @patch('apis.common_apis.check_connection')
    def test_health_check_disconnected(self, mock_check):
        mock_check.return_value = {"status": "error", "message": "Connection refused"}
        response = self.client.get('/apis/health/')
        self.assertEqual(response.status_code, 503)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'unhealthy')

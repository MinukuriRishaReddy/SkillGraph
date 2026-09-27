import hashlib
import logging

from models.connection import get_graph
from models.user import User
from utilities.query_for_services import (
    query_create_user, query_register, query_get_id_by_email,
    query_get_user_info, query_create_objective_career, query_get_objective,
    query_create_has_lo, query_create_user_need_lo,
    query_delete_relationship_user_need_lo, query_get_course_name_by_id,
    query_get_lo_user_has, query_get_lo_need_by_career_by_user_id
)
from services import igraph_service

logger = logging.getLogger(__name__)


def create_user(user, user_id):
    return get_graph().run(query_create_user(user_id, user.get('cost'), user.get('time'))).data()


def _hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def register(name, email, password):
    # Check if user already exists
    existing = get_graph().run(query_get_id_by_email(email)).data()
    if len(existing) > 0:
        return {}
    password_hash = _hash_password(password)
    return get_graph().run(query_register(name, email, password_hash)).data()


def update(user_id, career_id):
    from utilities.query_for_services import query_update_career
    get_graph().run(query_update_career(user_id, career_id))
    get_graph().run(query_create_objective_career(user_id, career_id))


def login(email, password):
    result = get_graph().run(query_get_id_by_email(email)).data()
    if len(result) > 0:
        stored_hash = result[0].get('password', '')
        if stored_hash and _hash_password(password) == stored_hash:
            return {"id": result[0].get("id")}
        else:
            return {"id": 0, "reason": "invalid_password"}
    else:
        return {"id": 0, "reason": "not_found"}


def get_user_info(user_id):
    result = get_graph().run(query_get_user_info(user_id)).data()
    if len(result) > 0:
        career = get_graph().run(query_get_objective(user_id)).data()
        if len(career) > 0:
            result[0]['career'] = career[0]
        else:
            result[0]['career'] = {}
        return User(result[0])
    else:
        return False


def create_objective_career(user_id, career_id):
    try:
        return get_graph().run(query_create_objective_career(user_id, career_id)).data()[0].get('id')
    except Exception as e:
        logger.error(f"Error creating objective career: {e}")
        return 0


def create_user_has_lo(user_id, list_lo):
    for lo in list_lo:
        get_graph().run(query_create_has_lo(user_id, lo))


def create_user_need_lo(user_id):
    for query in query_create_user_need_lo(user_id):
        get_graph().run(query).data()


def delete_user_need_lo(user_id):
    get_graph().run(query_delete_relationship_user_need_lo(user_id))


def get_learning_path(user_id):
    from algorithm_implementation import build_learning_path_step4
    user = User(get_graph().run(query_get_user_info(user_id)).data()[0])
    delete_user_need_lo(user_id)
    create_user_need_lo(user_id)
    lb = build_learning_path_step4.completing_step4(user)
    result = []
    counter = 1
    for path in lb:
        element = {
            "path": path,
            "visualization": f'/static/learning-path-{counter}.png'
        }
        try:
            igraph_service.visualize_learning_path_v1(get_course_name_by_id(path), counter)
        except Exception as e:
            logger.warning(f"Could not generate visualization: {e}")
            element["visualization"] = None
        result.append(element)
        counter += 1
    delete_user_need_lo(user_id)
    return result


def _map_name(d):
    return d.get('name')


def get_course_name_by_id(set_course):
    list_name = get_graph().run(query_get_course_name_by_id(set_course)).data()
    return [_map_name(n) for n in list_name]


def get_lo_need_by_user(user_id):
    user_lo = get_graph().run(query_get_lo_user_has(user_id)).data()
    career_lo = get_graph().run(query_get_lo_need_by_career_by_user_id(user_id)).data()
    lo_user_need = []
    for lo_career in career_lo:
        check = True
        for lo_user in user_lo:
            if lo_user.get('id') == lo_career.get('id') and lo_user.get('level') >= lo_career.get('level'):
                check = False
                break
        if check:
            lo_user_need.append(lo_career.copy())
    return lo_user_need


def get_learning_path_v2(user_id):
    from algorithm_v2.step3 import get_final_result
    from algorithm_v2.step2 import (
        calculate_number_of_course, calculate_number_of_redundant_LO,
        calculate_number_of_overlap_LO, calculate_sum_time_of_individual,
        calculate_sum_cost_of_individual
    )

    delete_user_need_lo(user_id)
    create_user_need_lo(user_id)
    try:
        paths = get_final_result(user_id)
    except Exception as e:
        logger.exception(f"Error generating learning path for user {user_id}")
        delete_user_need_lo(user_id)
        raise

    result = []
    counter = 1
    for path in paths:
        element = {
            "path": path,
            "visualization": f'/static/learning-path-{counter}.png'
        }
        try:
            igraph_service.visualize_learning_path_v2(path, counter)
        except Exception as e:
            logger.warning(f"Could not generate visualization: {e}")
            element["visualization"] = None
        result.append(element)
        counter += 1
    delete_user_need_lo(user_id)
    return result


def get_info_lp(courses, user_id):
    from algorithm_v2.step2 import (
        calculate_number_of_course, calculate_number_of_redundant_LO,
        calculate_number_of_overlap_LO, calculate_sum_time_of_individual,
        calculate_sum_cost_of_individual
    )

    delete_user_need_lo(user_id)
    create_user_need_lo(user_id)
    result = {
        'course': calculate_number_of_course(courses),
        'lor': calculate_number_of_redundant_LO(courses, get_lo_need_by_user(user_id)),
        'lod': calculate_number_of_overlap_LO(courses),
        'time': calculate_sum_time_of_individual(courses),
        'cost': calculate_sum_cost_of_individual(courses)
    }
    delete_user_need_lo(user_id)
    return result

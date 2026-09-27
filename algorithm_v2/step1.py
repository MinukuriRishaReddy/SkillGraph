"""
Algorithm V2 Step 1: Generate Candidate Courses

For each learning object (LO) the user needs, finds candidate courses
that can provide that LO, recursively resolving prerequisites.
"""
import itertools
import time
import logging

from models.connection import get_graph
from utilities import query_for_algorithm, query_algorithm_v2
from constants.algorithm_constants import AlgorithmConstant
from models.candidate import Candidate

logger = logging.getLogger(__name__)


def _get_list_id(list_dictionary):
    return [d.get('id') for d in list_dictionary]


def get_courses_without_similarity(courses_with_similarity):
    return [{'id': c.get('id')} for c in courses_with_similarity]


def get_user_lo_need(user_id):
    return get_graph().run(query_algorithm_v2.query_get_user_need_lo(user_id)).data()


def find_candidate_for_lo(lo):
    return get_graph().run(
        query_algorithm_v2.query_get_courses_provided_a_lo(lo.get('id'), lo.get('level'))
    ).data()


def get_top_n_candidate(user_id, courses):
    if not courses:
        return []
    return _get_list_id(
        get_graph().run(
            query_algorithm_v2.query_get_top_courses_with_overlap_similarity(
                user_id, _get_list_id(courses), AlgorithmConstant.V2_MUY
            )
        ).data()
    )


def get_los_required_by_course(courses):
    los_required = []
    for course in courses:
        los_required.extend(
            get_graph().run(query_algorithm_v2.query_get_input_lo_of_a_course(course)).data()
        )
    return los_required


def get_candidate_courses_all_los_required(user_id, los_required):
    candidate_courses = []
    for lo in los_required:
        candidates = find_candidate_for_lo(lo)
        top = get_top_n_candidate(user_id, candidates)
        if top:
            candidate_courses.append(top)
    return candidate_courses


def make_descartes_set_courses(candidate_courses):
    """Create Cartesian product of candidate courses."""
    if not candidate_courses:
        return []
    candidate_top_n = []
    for candidate in candidate_courses:
        n = max(1, round(AlgorithmConstant.V2_MUY / 3))
        candidate_top_n.append(candidate[:n])
    return [list(combo) for combo in itertools.product(*candidate_top_n)]


def create_temporary_relationship(user_id, user_lo_current_require):
    list_lo = _get_list_id(user_lo_current_require)
    if list_lo:
        get_graph().run(
            query_for_algorithm.query_to_create_temporary_relationship_user_lo(user_id, list_lo)
        )


def delete_temporary_relationship_created(user_id):
    get_graph().run(query_for_algorithm.query_to_remove_temporary_relationship_created(user_id))


def get_complete_candidate_for_a_lo(complete_candidates_courses, courses_extra, los_required,
                                     courses, user_id, user_lo_need, depth=0):
    """Recursively build complete candidate course sets for a single LO."""
    if depth > 10:  # Prevent infinite recursion
        logger.warning("Max recursion depth reached in candidate search")
        return

    for course in courses:
        courses_extra.append(course.copy())
        delete_temporary_relationship_created(user_id)

        new_los_required = get_los_required_by_course(course)
        if not new_los_required:
            complete_candidates_courses.append(courses_extra.copy())
            courses_extra.pop()
            continue
        else:
            create_temporary_relationship(user_id, new_los_required)
            sub_candidates = get_candidate_courses_all_los_required(user_id, new_los_required)
            descartes = make_descartes_set_courses(sub_candidates)
            get_complete_candidate_for_a_lo(
                complete_candidates_courses, courses_extra, new_los_required,
                descartes, user_id, user_lo_need, depth + 1
            )

    if courses_extra:
        courses_extra.pop()


def list_to_list_of_list(list_single):
    return [[single] for single in list_single]


def get_candidate_for_all_lo(los, user_id):
    """Get candidate courses for each LO the user needs."""
    start = time.time()
    list_candidate_all_los = []

    for lo in los:
        complete_candidate_courses = []
        candidates = find_candidate_for_lo(lo)
        top_candidates = get_top_n_candidate(user_id, candidates)

        if not top_candidates:
            logger.warning(f"No candidates found for LO {lo.get('id')}")
            list_candidate_all_los.append([])
            continue

        get_complete_candidate_for_a_lo(
            complete_candidate_courses, [], [],
            list_to_list_of_list(top_candidates),
            user_id, get_user_lo_need(user_id)
        )

        candidate_with_object = []
        for outer_course in complete_candidate_courses:
            content = []
            for inner_course in outer_course:
                if isinstance(inner_course, list):
                    content.extend(inner_course)
                else:
                    content.append(inner_course)
            candidate_with_object.append(Candidate(content, lo.get('id')))
        list_candidate_all_los.append(candidate_with_object)

    logger.info(f"Step 1 completed in {time.time() - start:.2f}s")
    return list_candidate_all_los


def get_input_for_step2(user_id):
    """Main entry point: generate candidate courses for all user LO needs."""
    lo_needs = get_user_lo_need(user_id)
    if not lo_needs:
        logger.warning(f"No LO needs found for user {user_id}")
        return []
    return get_candidate_for_all_lo(lo_needs, user_id)

import logging

from models.connection import get_graph
from utilities.query_for_services import query_get_info_a_course
from utilities.query_for_algorithm import query_get_lo_provided_by_course, query_lo_require_a_course

logger = logging.getLogger(__name__)


def get_lo_provided_by_course(course_id):
    return get_graph().run(query_get_lo_provided_by_course(course_id)).data()


def get_lo_required_by_course(course_id):
    return get_graph().run(query_lo_require_a_course(course_id)).data()


def get_info_course(course_id):
    result = get_graph().run(query_get_info_a_course(course_id)).data()
    if len(result) > 0:
        return result[0]
    return None

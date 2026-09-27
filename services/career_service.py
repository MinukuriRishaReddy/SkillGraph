import logging

from models.models import Career
from models.connection import get_graph
from utilities.query_for_services import query_get_lo_need_by_career, query_get_skill_learning_path

logger = logging.getLogger(__name__)


def get_all_career():
    all_career = Career.nodes.all()
    return [c.to_json_1() for c in all_career]


def get_career_by_id(career_id):
    career = Career.get_one(career_id)
    if career is None:
        return None
    return career.to_json_1()


def get_lo_career_need(career_id):
    return get_graph().run(query_get_lo_need_by_career(career_id)).data()


def get_skill_learning_path(career_id):
    result = get_graph().run(query_get_skill_learning_path(career_id)).data()
    if not result:
        return None
    row = result[0]
    # Filter out null relations from OPTIONAL MATCH
    relations = [r for r in (row.get('relations') or []) if r.get('source') and r.get('target')]
    return {
        'career': row.get('career', ''),
        'skills': row.get('skills') or [],
        'relations': relations,
    }

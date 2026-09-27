import logging

from models.connection import get_graph
from models.models import ProgramingLanguage, Knowledge, Framework, Platform, Tool
from utilities.query_for_services import (
    query_get_top_100_lo, query_search_lo, query_get_lo_has,
    query_delete_lo_has, query_create_lo_has, query_get_type
)

logger = logging.getLogger(__name__)


def get_all_programing_language():
    return [lang.to_json() for lang in ProgramingLanguage.nodes.all()]


def get_all_knowledge():
    return [k.to_json() for k in Knowledge.nodes.all()]


def get_all_tool():
    return [t.to_json() for t in Tool.nodes.all()]


def get_all_platform():
    return [p.to_json() for p in Platform.nodes.all()]


def get_all_framework():
    return [f.to_json() for f in Framework.nodes.all()]


def get_all_lo():
    return get_graph().run(query_get_top_100_lo()).data()


def get_lo_search(value):
    return get_graph().run(query_search_lo(value)).data()


def get_lo_has(user_id):
    return get_graph().run(query_get_lo_has(user_id)).data()


def delete_lo_has(user_id, lo_id):
    get_graph().run(query_delete_lo_has(user_id, lo_id))


def create_lo_has(user_id, lo_id, level):
    lo_type = get_graph().run(query_get_type(lo_id)).data()[0].get('type')
    return get_graph().run(query_create_lo_has(user_id, lo_id, level, lo_type)).data()

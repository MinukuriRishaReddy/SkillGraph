from django.urls import path
from . import career_apis, learning_object_apis, user_apis, course_apis, common_apis, chatbot_apis

urlpatterns = [
    # Health check
    path('health/', common_apis.health_check),

    # Chatbot endpoint
    path('chatbot/chat', chatbot_apis.chat),

    # Career endpoints
    path('career/', career_apis.get_all_career),
    path('career/one', career_apis.get_career_by_id),
    path('career/lo', career_apis.get_lo_need),
    path('learning-path', career_apis.get_skill_learning_path),

    # Learning Object endpoints
    path('lo/all', learning_object_apis.get_search_lo),
    path('lo/language/', learning_object_apis.get_all_programing_language),
    path('lo/knowledge', learning_object_apis.get_all_knowledge),
    path('lo/tool', learning_object_apis.get_all_tool),
    path('lo/platform', learning_object_apis.get_all_platform),
    path('lo/framework', learning_object_apis.get_all_framework),

    # Course endpoints
    path('course', course_apis.get_info_course),
    path('course/provided/lo', course_apis.get_lo_provided_by_course),
    path('course/required/lo', course_apis.get_lo_required_by_course),

    # User endpoints
    path('user/login', user_apis.login),
    path('user/register', user_apis.register),
    path('user/create', user_apis.create_user),
    path('user/info/', user_apis.get_user_info),
    path('user/objective', user_apis.create_objective_career),
    path('user/career/update', user_apis.update),
    path('user/need', user_apis.get_lo_need_by_user),
    path('user/lp', user_apis.get_lp_info),
    path('user/learning-path', user_apis.get_learning_path),

    # User LO management (GET vs POST handled in view)
    path('user/has', learning_object_apis.handle_user_has),
    path('user/has/create', learning_object_apis.create_lo_has),
    path('user/has/delete', learning_object_apis.delete_lo_has),
]

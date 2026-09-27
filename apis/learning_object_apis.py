import json
import logging

from django.http import JsonResponse

from services import learning_object_service

logger = logging.getLogger(__name__)


def get_all_programing_language(request):
    try:
        return JsonResponse(learning_object_service.get_all_programing_language(), safe=False)
    except Exception as e:
        logger.exception("Error fetching programming languages")
        return JsonResponse({"error": str(e)}, status=500)


def get_all_knowledge(request):
    try:
        return JsonResponse(learning_object_service.get_all_knowledge(), safe=False)
    except Exception as e:
        logger.exception("Error fetching knowledge LOs")
        return JsonResponse({"error": str(e)}, status=500)


def get_all_tool(request):
    try:
        return JsonResponse(learning_object_service.get_all_tool(), safe=False)
    except Exception as e:
        logger.exception("Error fetching tools")
        return JsonResponse({"error": str(e)}, status=500)


def get_all_platform(request):
    try:
        return JsonResponse(learning_object_service.get_all_platform(), safe=False)
    except Exception as e:
        logger.exception("Error fetching platforms")
        return JsonResponse({"error": str(e)}, status=500)


def get_all_framework(request):
    try:
        return JsonResponse(learning_object_service.get_all_framework(), safe=False)
    except Exception as e:
        logger.exception("Error fetching frameworks")
        return JsonResponse({"error": str(e)}, status=500)


def get_search_lo(request):
    try:
        value = request.GET.get('value', '')
        if not value:
            return JsonResponse(learning_object_service.get_all_lo(), safe=False)
        return JsonResponse(learning_object_service.get_lo_search(value), safe=False)
    except Exception as e:
        logger.exception("Error searching LOs")
        return JsonResponse({"error": str(e)}, status=500)


def handle_user_has(request):
    """Combined handler for GET /apis/user/has and POST /apis/user/has."""
    if request.method == 'GET':
        return get_lo_has(request)
    elif request.method == 'POST':
        return _create_user_has_lo(request)
    return JsonResponse({"error": "Method not allowed"}, status=405)


def get_lo_has(request):
    try:
        user_id = request.GET.get('id')
        if not user_id:
            return JsonResponse({"error": "Missing required parameter: id"}, status=400)
        return JsonResponse(learning_object_service.get_lo_has(int(user_id)), safe=False)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching user LOs")
        return JsonResponse({"error": str(e)}, status=500)


def _create_user_has_lo(request):
    """Handle POST to /apis/user/has — add multiple LOs to user."""
    try:
        body = json.loads(request.body.decode('utf-8'))
        user_id = body.get('user_id')
        list_lo = body.get('list_lo')
        if not user_id or not list_lo:
            return JsonResponse({"error": "Missing user_id or list_lo"}, status=400)
        from services import user_service
        user_service.create_user_has_lo(user_id, list_lo)
        return JsonResponse({"message": "succeed"}, status=200)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": f"Invalid request body: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error creating user LO relationships")
        return JsonResponse({"error": str(e)}, status=500)


def delete_lo_has(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        user_id = body.get('user')
        lo_id = body.get('lo')
        if user_id is None or lo_id is None:
            return JsonResponse({"error": "Missing user or lo parameter"}, status=400)
        learning_object_service.delete_lo_has(int(user_id), int(lo_id))
        return JsonResponse({"msg": "success"})
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": f"Invalid request body: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error deleting user LO")
        return JsonResponse({"error": str(e)}, status=500)


def create_lo_has(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        user_id = body.get('user')
        lo_id = body.get('lo')
        level = body.get('level')
        if user_id is None or lo_id is None or level is None:
            return JsonResponse({"error": "Missing user, lo, or level parameter"}, status=400)
        learning_object_service.delete_lo_has(int(user_id), int(lo_id))
        result = learning_object_service.create_lo_has(int(user_id), int(lo_id), int(level))
        return JsonResponse(result, safe=False)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": f"Invalid request body: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error creating LO has relationship")
        return JsonResponse({"error": str(e)}, status=500)

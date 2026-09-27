import json
import logging

from django.http import JsonResponse

from services import user_service
from models.user import User

logger = logging.getLogger(__name__)


def create_user(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        user_id = body.get('id')
        if user_id is None:
            return JsonResponse({"error": "Missing required field: id"}, status=400)
        user = {
            'name': body.get('name', 'anonymous'),
            'email': body.get('email', 'anonymous'),
            'cost': int(body.get('cost', 0)),
            'time': int(body.get('time', 0)),
        }
        result = user_service.create_user(user, int(user_id))
        if len(result) > 0:
            return JsonResponse(result[0], status=200)
        else:
            return JsonResponse({"message": "failed"}, status=400)
    except (json.JSONDecodeError, ValueError) as e:
        return JsonResponse({"error": f"Invalid request: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error creating user")
        return JsonResponse({"error": str(e)}, status=500)


def register(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        name = body.get('name')
        email = body.get('email')
        password = body.get('password')
        if not name or not email or not password:
            return JsonResponse({"error": "Missing name, email, or password"}, status=400)
        if len(password) < 6:
            return JsonResponse({"error": "Password must be at least 6 characters"}, status=400)
        result = user_service.register(name, email, password)
        if len(result) > 0:
            return JsonResponse(result[0], status=200)
        else:
            return JsonResponse({"message": "User already exists"}, status=400)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": f"Invalid request: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error registering user")
        return JsonResponse({"error": str(e)}, status=500)


def update(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        user_id = body.get('user')
        career_id = body.get('career')
        if user_id is None or career_id is None:
            return JsonResponse({"error": "Missing user or career"}, status=400)
        user_service.update(int(user_id), int(career_id))
        return JsonResponse({"msg": "success"}, status=200)
    except (json.JSONDecodeError, ValueError) as e:
        return JsonResponse({"error": f"Invalid request: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error updating user career")
        return JsonResponse({"error": str(e)}, status=500)


def login(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        email = body.get('email')
        password = body.get('password')
        if not email or not password:
            return JsonResponse({"error": "Missing email or password"}, status=400)
        result = user_service.login(email, password)
        if result.get("id") and result["id"] != 0:
            return JsonResponse({"id": result["id"]}, status=200)
        reason = result.get("reason", "not_found")
        if reason == "invalid_password":
            return JsonResponse({"error": "Invalid email or password"}, status=401)
        return JsonResponse({"error": "No account found with this email"}, status=404)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": f"Invalid request: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error during login")
        return JsonResponse({"error": str(e)}, status=500)


def get_user_info(request):
    try:
        user_id = request.GET.get("id")
        if not user_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        result = user_service.get_user_info(int(user_id))
        if isinstance(result, User):
            return JsonResponse(result.get_user(), safe=False)
        else:
            return JsonResponse({"message": "User not found"}, status=404)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching user info")
        return JsonResponse({"error": str(e)}, status=500)


def create_objective_career(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        user_id = body.get('user_id')
        career_id = body.get('career_id')
        if user_id is None or career_id is None:
            return JsonResponse({"error": "Missing user_id or career_id"}, status=400)
        result = user_service.create_objective_career(int(user_id), int(career_id))
        if result > 0:
            return JsonResponse({"id": result})
        else:
            return JsonResponse({"message": "failed"}, status=400)
    except (json.JSONDecodeError, ValueError) as e:
        return JsonResponse({"error": f"Invalid request: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error creating objective")
        return JsonResponse({"error": str(e)}, status=500)


def create_user_has_lo(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        user_id = body.get("user_id")
        list_lo = body.get("list_lo")
        if user_id is None or not list_lo:
            return JsonResponse({"error": "Missing user_id or list_lo"}, status=400)
        user_service.create_user_has_lo(int(user_id), list_lo)
        return JsonResponse({"message": "succeed"}, status=200)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": f"Invalid request: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error creating user LO")
        return JsonResponse({"error": str(e)}, status=500)


def get_lo_need_by_user(request):
    try:
        user_id = request.GET.get('id')
        if not user_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        return JsonResponse(user_service.get_lo_need_by_user(int(user_id)), safe=False, status=200)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching user LO needs")
        return JsonResponse({"error": str(e)}, status=500)


def get_learning_path(request):
    try:
        user_id = request.GET.get("id")
        if not user_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        lb = user_service.get_learning_path_v2(int(user_id))
        return JsonResponse(lb, safe=False)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error generating learning path")
        return JsonResponse({"error": str(e)}, status=500)


def get_lp_info(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        courses = body.get('courses')
        user_id = body.get('user')
        if not courses or user_id is None:
            return JsonResponse({"error": "Missing courses or user"}, status=400)
        return JsonResponse(user_service.get_info_lp(courses, int(user_id)), safe=False)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": f"Invalid request: {e}"}, status=400)
    except Exception as e:
        logger.exception("Error fetching LP info")
        return JsonResponse({"error": str(e)}, status=500)

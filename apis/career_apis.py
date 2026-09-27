import logging

from django.http import JsonResponse

from services import career_service

logger = logging.getLogger(__name__)


def get_all_career(request):
    try:
        return JsonResponse(career_service.get_all_career(), safe=False)
    except Exception as e:
        logger.exception("Error fetching careers")
        return JsonResponse({"error": str(e)}, status=500)


def get_career_by_id(request):
    try:
        career_id = request.GET.get("id")
        if not career_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        result = career_service.get_career_by_id(int(career_id))
        if result is None:
            return JsonResponse({"error": "Career not found"}, status=404)
        return JsonResponse(result, safe=False)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching career")
        return JsonResponse({"error": str(e)}, status=500)


def get_lo_need(request):
    try:
        career_id = request.GET.get("id")
        if not career_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        return JsonResponse(career_service.get_lo_career_need(int(career_id)), safe=False, status=200)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching career LO needs")
        return JsonResponse({"error": str(e)}, status=500)


def get_skill_learning_path(request):
    try:
        career_id = request.GET.get("id")
        if not career_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        result = career_service.get_skill_learning_path(int(career_id))
        if result is None:
            return JsonResponse({"error": "Career not found"}, status=404)
        return JsonResponse(result, safe=False)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching skill learning path")
        return JsonResponse({"error": str(e)}, status=500)

import logging

from django.http import JsonResponse

from services import course_service

logger = logging.getLogger(__name__)


def get_lo_provided_by_course(request):
    try:
        course_id = request.GET.get('id')
        if not course_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        return JsonResponse(course_service.get_lo_provided_by_course(int(course_id)), safe=False, status=200)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching course provided LOs")
        return JsonResponse({"error": str(e)}, status=500)


def get_lo_required_by_course(request):
    try:
        course_id = request.GET.get('id')
        if not course_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        return JsonResponse(course_service.get_lo_required_by_course(int(course_id)), safe=False, status=200)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching course required LOs")
        return JsonResponse({"error": str(e)}, status=500)


def get_info_course(request):
    try:
        course_id = request.GET.get('id')
        if not course_id:
            return JsonResponse({"error": "Missing id parameter"}, status=400)
        result = course_service.get_info_course(int(course_id))
        if result is None:
            return JsonResponse({"error": "Course not found"}, status=404)
        return JsonResponse(result, safe=False, status=200)
    except ValueError:
        return JsonResponse({"error": "Invalid id parameter"}, status=400)
    except Exception as e:
        logger.exception("Error fetching course info")
        return JsonResponse({"error": str(e)}, status=500)

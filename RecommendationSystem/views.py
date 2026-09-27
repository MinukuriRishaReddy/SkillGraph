from django.http import JsonResponse
from models.connection import check_connection


def index(request):
    return JsonResponse({
        "name": "Learning Path Recommendation System API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "careers": "/apis/career/",
            "learning_objects": "/apis/lo/all",
            "users": "/apis/user/login",
            "health": "/apis/health/",
            "swagger": "/swagger/",
            "admin": "/admin/"
        }
    })

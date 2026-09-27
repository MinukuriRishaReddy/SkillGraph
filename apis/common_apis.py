from django.http import JsonResponse
from models.connection import check_connection


def health_check(request):
    """Health check endpoint that tests Neo4j connectivity."""
    db_status = check_connection()
    status_code = 200 if db_status['status'] == 'connected' else 503
    return JsonResponse({
        "status": "healthy" if status_code == 200 else "unhealthy",
        "database": db_status,
    }, status=status_code)

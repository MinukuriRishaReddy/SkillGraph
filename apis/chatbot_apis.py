from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from services.chatbot_service import get_tutor_response

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            messages = data.get('messages', [])
            response = get_tutor_response(messages)
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

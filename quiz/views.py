from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def get_question(request):
    if request.method == 'GET':
        data = {
            "id": 1,
            "text": "ประเทศไทยมีกี่จังหวัด",
            "choices": [50, 68, 72, 77]
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    

@csrf_exempt
def create_question(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            return JsonResponse(body, status=201, json_dumps_params={'ensure_ascii': False})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON ไม่ถูกต้อง"}, status=400, json_dumps_params={'ensure_ascii': False})

        
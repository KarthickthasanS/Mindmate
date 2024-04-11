from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import re
# Create your views here.

def aichat(request):
    return render(request, "aichat.html")

url = ''



logger = logging.getLogger(__name__)
@csrf_exempt
def update_url(request):
    global url
    if request.method == 'POST':
        url = request.POST.get('url')
        return JsonResponse({"message": "URL updated successfully"}, status=200)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
    

@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        if not prompt:
            return JsonResponse({"error": "Prompt not provided"}, status=400)

        
        headers = {'Content-Type': 'application/json'}
        body = {'inputs': prompt}  # Add your JSON data here

        try:
            response = requests.post(url, headers=headers, data=json.dumps(body))
            response.raise_for_status()  # Raise exception for non-200 status codes
            generated_text = response.json()['generated_texts'][0]
            


            return JsonResponse({"answer": generated_text}, status=200)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request to {url} failed: {e}")
            return JsonResponse({"error": "Error generating text"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
    

    

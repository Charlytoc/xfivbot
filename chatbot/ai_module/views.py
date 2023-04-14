from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def answer_from_a_template(request):
    """
    This view is to provide an answer based in a template, it will receive two inputs:
    REQUEST BODY
    {
        prompt_id= int,
        user_input = str
    }
    And will return an answer in str format like:
    RESPONSE BODY
    {
        ai_answer: str,
        status: int,
    }
    """

    if request.method == 'POST':
        request_data = json.loads(request.body)
        prompt_id = request_data.get('prompt_id')
        user_input = request_data.get('user_input')
        print(prompt_id, user_input)
        # TODO: process user input and generate an AI answer
        
        ai_answer = "This is a sample answer"
        status = 200
        
        response_data = {
            'ai_answer': ai_answer,
            'status': status,
        }
        return JsonResponse(response_data)
    else:
        # Handle other HTTP methods (e.g. GET, PUT, DELETE)
        # by returning a 405 Method Not Allowed status code
        return JsonResponse({'error': 'Method not allowed'}, status=405)


    
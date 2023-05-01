
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from firststep.secrets import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        input_text = request.POST.get("input", "")
        response_text = get_chatbot_response(input_text)
        return JsonResponse({"response": response_text})
    else:
        return JsonResponse({"error": "Invalid request method"})


def get_chatbot_response(input_text):
    model_engine = "text-davinci-002"
    prompt = input_text.strip()
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the API response
    response_text = response.choices[0].text.strip()

    return response_text




# # from django.http import HttpResponse
# # from django.shortcuts import render
# # import requests
# # from django.shortcuts import render
# # from .utils import chat_with_gpt

# import openai
# from django.http import JsonResponse

# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST

# from .utils import get_chatbot_response

# # Set up the OpenAI API client
# openai.api_key = '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'

# # Define a view to handle chatbot requests
# @csrf_exempt
# @require_POST
# def chatbot(request):
#     # Get the user's input from the request body
#     input_text = request.POST["input"]

#     # Use the OpenAI API to generate a response
#     response_text = get_chatbot_response(input_text)

#     # Return the response as JSON
#     return JsonResponse({"response": response_text})


# # def home(request):
# #     return HttpResponse ('home to Saudi')

# # def home3(request):
# #    data={
# #        'title': 'Assalamualaikum!!!!',
# #        'b': 'welcome to our society 2023',
# #        'age': [10,20,30,40,50,60,70,80,90,100],
# #        'course': ['PHP', 'JAVA', 'PYTHON'],
# #        'student_details':[
# #        {'name': 'Maruf', 'phone': 1821629125},
# #        {'name': 'Munna', 'phone': 1780553637},
# #        {'name': 'Mahid', 'phone': 1751933365}  
# #        ]
# #    }
# #    return render(request,'index.html', data)
   

        


# # def chat_with_gpt(input_text):
# #     # Set the API endpoint URL
# #     url = 'https://api.openai.com/v1/engine/davinci-codex/completions'

# #     # Set the headers with your API key
# #     headers = {
# #         'Content-Type': 'application/json',
# #         'Authorization': 'Bearer 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'
# #     }

# #     # Set the request data with the input text and parameters
# #     data = {
# #         'prompt': input_text,
# #         'max_tokens': 100,
# #         'temperature': 0.5
# #     }

# #     # Make the POST request to the API endpoint
# #     response = requests.post(url, headers=headers, json=data)

# #     # Extract the generated text from the API response
# #     generated_text = response.json()['choices'][0]['text']

# #     # Return the generated text
# #     return generated_text




# # # def chat_with_gpt_view(request):
# # #     if request.method == 'POST':
# # #         # Get the input text from the form submission
# # #         input_text = request.POST.get('input_text')

# # #         # Generate a response using the ChatGPT API
# # #         generated_text = chat_with_gpt(input_text)

# # #         # Render the template with the generated text
# # #         return render(request, 'chat_with_gpt.html', {'generated_text': generated_text})
# # #     else:
# # #         # Render the empty form
# # #         return render(request, 'chat_with_gpt.html')


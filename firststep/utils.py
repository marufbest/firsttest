# import openai
# openai.api_key = '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'

# def chat_with_gpt(input_text):
#     response = openai.Completion.create(
#         engine='davinci',
#         prompt=input_text,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     return response.choices[0].text.strip()

import openai
import os

openai.api_key = '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'

def chat_with_gpt(input_text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Conversation with a chatbot:\nUser: {input_text}\nChatbot:",
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    message = response.choices[0].text.strip()
    return message


# import requests

# def chat_with_gpt(input_text):
#     # Set the API endpoint URL
#     url = 'https://api.openai.com/v1/engine/davinci-codex/completions'

#     # Set the headers with your API key
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer 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'
#     }

#     # Set the request data with the input text and parameters
#     data = {
#         'prompt': input_text,
#         'max_tokens': 100,
#         'temperature': 0.5
#     }

#     # Make the POST request to the API endpoint
#     response = requests.post(url, headers=headers, json=data)

#     # Extract the generated text from the API response
#     generated_text = response.json()['choices'][0]['text']

#     # Return the generated text
#     return generated_text

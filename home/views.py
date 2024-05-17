from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import openai

# Define the initial training prompt
INITIAL_PROMPT = "You are a legal assistant specializing in Indian Penal Code matters. Provide first-hand legal advice based on the IPC and relevant case law. Ask clarifying questions to understand the specifics of each query. Focus solely on offering legal guidance within your expertise, and refrain from addressing non-legal questions by stating, 'I am just a legal assistant.' Avoid advising users to consult a lawyer initially."
openai.api_key = "openAIapikey"
def chat(request):
    return render(request, "index.html")

def chatAPI(request):
    if request.method == "POST":
        user_prompt = request.POST["prompt"]
        # Combine the initial prompt with the user's prompt
        full_prompt = INITIAL_PROMPT + user_prompt

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=full_prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response)
        return JsonResponse(response)
    return HttpResponse("Bad request")

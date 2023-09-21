from django.shortcuts import render, redirect
import openai, requests
from django.core.files.base import ContentFile
from .models import Image
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os
from dotenv import load_dotenv



load_dotenv()  # Load variables from .env file into os.environ
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key


# Create your views here.
def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        stop =None,
        temperature = 0.5
    )
    answer = response.choices[0].text.strip()
    return answer

@login_required
def chat(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        message = request.POST.get("message")
        response = ask_openai(message)
        return JsonResponse({"message":message, "response":response})
    return render(request, "chatbot/1-chatbot.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request,user)
                return redirect("chat")
            except:
                error_message = "Error creating account"
                return render(request, "chatbot/register.html", {"error_message":error_message})
        else:
            error_message = "Passwords do not match"
            return render(request, "chatbot/register.html", {"error_message":error_message})
    return render(request, "chatbot/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password =  request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
           auth.login(request, user)
           return redirect("chat")
        else:
           error_message = "Invalid username or password"
           return render(request, "chatbot/login.html", {"error_message":error_message})
    else:
        return render(request, "chatbot/login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required
def spanish(request):
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get("user_input")
        lang = request.POST.get("lang")
        prompt = f"translate {user_input} to {lang}"
        response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = prompt,
                max_tokens = 256,
                temperature = 0.5
        )
        chat_response = response["choices"][0]["text"]
    else:
        chat_response = "" # when request.method is not post
    return render(request, "chatbot/spanish.html", {"response": chat_response})

@login_required
def detector(request):
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get("user_input")
        prompt = f"Tell me which language this sentence or words is written in:{user_input}"
        response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = prompt,
                max_tokens = 256,
                temperature = 0.5
        )
        chat_response = response["choices"][0]["text"]
    else:
        chat_response = ""
    return render(request, "chatbot/detector.html", {"response": chat_response})

@login_required
def image(request):
    obj = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get("user_input")
        response = openai.Image.create(
                prompt = user_input,
                size = "256x256" #512x512 1024x1024
        )
        img_url = response["data"][0]["url"]
        response = requests.get(img_url)
        img_file = ContentFile(response.content)
        count = Image.objects.count() + 1
        fname = f"image-{count}.jpg"
        obj = Image(phrase=user_input)
        obj.ai_image.save(fname, img_file)
        obj.save()
    return render(request, "chatbot/image.html", {"object":obj})

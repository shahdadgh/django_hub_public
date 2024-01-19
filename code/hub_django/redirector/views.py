from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def redirect_app1(request):
    return redirect('/app1/')

def redirect_app2(request):
    return redirect('/app2/')

def redirect_app3(request):
    return redirect('/app3/')

def redirect_chatbot_frontend(request):
    return redirect('/genai/home/')

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def login(request):
    return redirect('polls:login_success')

def login_success(request):
    return render(request, "login_success.html")
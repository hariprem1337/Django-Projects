from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    return render(request,"index.html")

def signinUser(request):
    user_id = request.POST.get("user_name")
    pw = request.POST.get("password")
    message = "Welcome to the Home Page"
    return HttpResponse(message)
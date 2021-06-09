from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    return render(request, "index.html")

def registerUser(request):
    f_name = request.POST.get("first_name")
    l_name = request.POST.get("last_name")
    email = request.POST.get("email_id")
    phone_no = request.POST.get("phone_number")

    full_name = f_name +' '+ l_name
    return HttpResponse("Welcome"+" "+full_name)


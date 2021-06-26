from django.shortcuts import render
from app19.models import Registration

def showHome(request):
    return render(request, "home.html")
def showCovid(request):
    return render(request, "corona.html")
def showRegister(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        n = request.POST.get("name")
        e = request.POST.get("email")
        con = request.POST.get("contact")
        loc = request.POST.get("location")
        pw = request.POST.get("password")

        Registration(name=n, email=e, contact=con, location=loc, password=pw).save()
        return render(request, "register.html", {"message" : "Registration is Done"})
def showLogin(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        e = request.POST.get("email")
        pw = request.POST.get("password")

        try:
            user_obj = Registration.objects.get(email=e, password=pw)
            return render(request, "welcome.html")
        except Registration.DoesNotExist:
            return render(request, "login.html", {"message": "Invalid User"})
def showContact(request):
    return render(request, "contact.html")

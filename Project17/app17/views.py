from django.shortcuts import render
from app17.models import Register

def showHome(request):
    return render(request, "home.html")
def showRegister(request):
    if request.method=="GET":
        return render(request, "register.html")
    else:
        nam = request.POST.get("name")
        em = request.POST.get("email")
        con = request.POST.get("number")
        loc = request.POST.get("location")
        pw = request.POST.get("password")

        Register(name=nam, email=em, contact=con, location=loc, password=pw).save()
        return render(request, "register.html", {"message": "Registration was Completed"})
def showLogin(request):
    if request.method=="GET":
        return render(request, "login.html")
    else:
        em = request.POST.get("email")
        pw = request.POST.get("password")
        try:
            user_obj = Register.objects.get(email=em, password=pw)
            return render(request, "welcome.html")
        except Register.DoesNotExist:
            return render(request, "login.html", {"message":"Invalid User"})



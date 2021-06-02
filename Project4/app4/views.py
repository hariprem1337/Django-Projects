from django.shortcuts import render

def showIndex(request):
    return render(request, "Registration_form.html")

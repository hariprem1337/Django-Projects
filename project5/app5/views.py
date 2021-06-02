from django.shortcuts import render

def showIndex(request):
    return render(request,"home_needs.html")

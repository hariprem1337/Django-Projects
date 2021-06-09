from django.shortcuts import render

def showIndex(request):
    return render(request, "index.html")

def checkUser(request):
    user_name = request.POST.get("u_name")
    password = request.POST.get("pw")

    if user_name == "HariPrem" and password == "123456":
        return render(request, "home.html", {"data" : user_name})
    else:
        return render(request, "error.html")

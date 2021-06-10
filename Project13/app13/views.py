from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        user_name = request.POST.get("u_name")
        password = request.POST.get("pw")
        if user_name == "HariPrem" and password == "123456":
            return render(request, "index.html", {"message" : "True"})
        else:
            return render(request, "index.html", {"message" : "False"})
    else:
        return render(request, "index.html")

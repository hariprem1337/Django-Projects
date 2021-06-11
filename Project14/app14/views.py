from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        user_name = request.POST.get("u_name")
        password = request.POST.get("pw")
        user_type = request.POST.get("type")
        if user_name == "Ravi":
           if password == "ravi1234@" and user_type == "Admin":
               return render(request, "welcome.html" , {"message" : "admin"})
           elif password == "kumar@123" and user_type == "Employee":
               return render(request, "welcome.html", {"message" : "employee" })
           elif password == "ravikumar@123" and user_type == "Customer":
               return render(request, "welcome.html", {"message" : "customer"})
           else:
               return render(request, "index.html", {"data" : "False"})
        else:
            return render(request, "index.html", {"data": "False"})
    else:
        return render(request, "index.html")

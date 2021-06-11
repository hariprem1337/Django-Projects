from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        number1 = request.POST.get("num1")
        number2 = request.POST.get("num2")
        button = request.POST.get("oper")
        pass
    else:
        return render(request, "index.html")

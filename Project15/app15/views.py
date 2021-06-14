from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        number1 = request.POST.get("num1")
        number2 = request.POST.get("num2")
        add_button = request.POST.get("cal1")
        sub_button = request.POST.get("cal2")
        mul_button = request.POST.get("cal3")
        div_button = request.POST.get("cal4")
        if add_button:
            res = int(number1) + int(number2)
            return render(request, "index.html", {"message": "add" , "value" : res})
        elif sub_button:
            res = int(number1) - int(number2)
            return render(request, "index.html", {"message": "sub" , "value" : res})
        elif mul_button:
            res = int(number1) * int(number2)
            return render(request, "index.html", {"message": "mul" , "value" : res})
        else:
            res = int(number1) / int(number2)
            return render(request, "index.html", {"message": "div" , "value" : res})
    else:
        return render(request, "index.html")

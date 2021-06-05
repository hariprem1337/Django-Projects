from django.shortcuts import render

def showIndex(request):
    students_info = [
        {"idno":101 , "name":"Hari" , "marks":[97,56,72,83,55]},
        {"idno":102 , "name":"Prem" , "marks":[68,42,24,74,88]},
        {"idno":103 , "name":"Karthik" , "marks":[79,16,52,48,90]},
        {"idno":104 , "name":"Anil" , "marks":['A',26,38,62,77]},
        {"idno":105 , "name":"Prasad" , "marks":[45,82,'A',56,78]},
        ]
    data_info = {"data" : students_info}
    return render(request, "main.html", data_info)

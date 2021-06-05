from django.shortcuts import render

def showIndex(request):
    emps_info = [
        {"idno":101 , "name":"Hari Prem" , "salary":200000.00},
        {"idno":102 , "name":"Karthik" , "salary":250000.00},
        {"idno":103 , "name":"Charan" , "salary":300000.00},
        {"idno":104 , "name":"Ashok" , "salary":180000.00},
        {"idno":105 , "name":"Sai" , "salary":150000.00},
        ]
    return render(request, "main.html", {"data":emps_info})

from django.shortcuts import render

def showIndex(request):
    emps_info = {
            101 : {"name1":"Hari Prem" , "salary1":200000.00},
            102 : {"name2":"Karthik" , "salary2":250000.00},
            103 : {"name3":"Charan" , "salary3":300000.00},
            104 : {"name4":"Ashok" , "salary4":180000.00},
            105 : {"name5":"Sai" , "salary5":150000.00},
        }
    return render(request, "main.html", emps_info)

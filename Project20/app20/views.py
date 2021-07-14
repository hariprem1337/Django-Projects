from django.shortcuts import render, redirect
from app20.models import StudentRegisterModel

def showHome(request):
    return render(request, "home.html")

def saveStudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        photo = request.FILES['photo']
        dob = request.POST.get("dob")
        location = request.POST.get("location")
        password = request.POST.get("password")
        StudentRegisterModel(name=name, email=email, contact=contact, photo=photo, dob=dob, location=location, password=password).save()
        return render(request, "home.html", {"message": "Your registration was successful"})
    else:
        return redirect('home')
def showDisplay(request):
    return render(request, "display.html", {"student_info": StudentRegisterModel.objects.all()})

def deleteStudent(request, student_number):
    stu_data = StudentRegisterModel.objects.get(number=student_number)
    if request.method == "POST":
        stu_data.delete()
        return render(request, "display.html", {"student_info": StudentRegisterModel.objects.all()})
    else:
        return render(request, "delete_student.html", {"student_info":stu_data})
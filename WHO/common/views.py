from django.shortcuts import render
from django.shortcuts import redirect
from student.models import RegisterModel
from django.db.models import Q
from random import randint
from django.contrib import messages
from common.utils import sendTextMessage

def showHome(request):
    return render(request, "common/home.html")
def showCovid(request):
    return render(request, "common/covid.html")
def showStudent(request):
    return render(request, "common/student.html")
def showStudentRegistration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("number")
        password = request.POST.get("password")

        record = RegisterModel.objects.filter(Q(email=email) | Q(contact=contact))
        if record:
            return render(request, "common/student.html", {"data":[name, email, contact, "Email or Contact Number was already available"]})
        else:
            otp = randint(10000, 99999)

            message = '''Thanks for Registered With World Health Organization (WHO), 
            To complete your Registration use the given OTP.
            Your OTP : ''' + str(otp)

            if sendTextMessage(message, contact):
                RegisterModel(name=name, email=email, contact=contact, password=password, otp=otp).save()
                messages.success(request, contact)
                return redirect('student_otp')
            else:
                return render(request, "common/student.html", {"data": [name, email, contact, "Wrong Contact Number"]})
    else:
        showStudent(request)
def showOTP(request):
    return render(request, "common/otp.html")
def showDoctor(request):
    return render(request, "common/doctor.html")
def showAdmin(request):
    return render(request, "common/admin.html")
def showContact(request):
    return render(request, "common/contact.html")
def validateStudentOTP(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        student_otp = request.POST.get("student_otp")
        try:
            result = RegisterModel.objects.get(contact=contact, otp=student_otp)
            result.status = "Active"
            result.save()
            return render(request, "common/student.html", {"message":"Your Registration was Successful : Please Login"})
        except RegisterModel.DoesNotExist:
            messages.success(request, contact)
            return redirect('student_otp')
    else:
        return render(request, "common/otp.html")

def showStudentLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            stu_details = RegisterModel.objects.get(email=email, password=password)
            return render(request, "student/student_welcome.html")
        except RegisterModel.DoesNotExist:
            return render(request, "common/student.html", {"error_msg": "Invalid User"})
from django.shortcuts import render
from django.shortcuts import redirect
from student.models import RegistrationModel
from random import randint
from common.utils import sendTextMessage
from django.db.models import Q

def showHome(request):
    return render(request, "common/home.html")
def showAdmin(request):
    return render(request, "common/admin.html")
def showFaculty(request):
    return render(request, "common/faculty.html")
def showContact(request):
    return render(request, "common/contact.html")
def showStudent(request):
    return render(request, "common/student.html")
def showStudentRegistration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("number")
        password = request.POST.get("password")

        record = RegistrationModel.objects.filter(Q(contact=contact) | Q(email=email))
        if record:
            return render(request, "common/student.html", {"data":[name,contact,email,"Email or Contact Number was already available"]})
        else:
            otp = randint(1000, 99999)

            message = '''Thanks for Registered With SathyaTech,
                To complete your Registration Use the Given OTP
                Your OTP : ''' + str(otp)
            if sendTextMessage(message, contact):
                RegistrationModel(name=name, email=email, contact=contact, password=password).save()
                return redirect('student_otp')
            else:
                return render(request, "common/student.html", {"data":[name,contact,email,"Wrong Contact Number"]})
    else:
        showStudent(request)

def showOTP(request):
    return render(request, "common/otp.html")


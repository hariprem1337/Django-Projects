from django.shortcuts import render

def showHome(request):
    return render(request, "common/home.html")
def showAdmin(request):
    return render(request, "common/admin.html")
def showFaculty(request):
    return render(request, "common/faculty.html")
def showStudent(request):
    return render(request, "common/student.html")
def showContact(request):
    return render(request, "common/contact.html")

from django.shortcuts import render
from django.http import HttpResponse
from myFirstApp.models import Student


# Create your views here.

def Hello(request):
    msg = "Welcome to My First Application"
    return HttpResponse(msg)


def index(request):
    return render(request, 'index.html', {"name": "Rusiru Fernando", "intro": "Coder | Gamer | Foodie"})


def savedata(request):
    r = 'R1001'
    n = "Rusiru Fernando"
    a = "LK 001"
    c = "Negombo"
    obj = Student(rollno=r, name=n, address=a, city=c)
    obj.save()
    msg = "Data saved now"
    return HttpResponse(msg)


def showdata(request):
    obj = Student.objects.all()
    msg = "Data...<br/>"
    for res in obj:
        msg = msg + res.rollno + "<br/>"
        msg = msg + res.name + "<br/>"
        msg = msg + res.address + "<br/>"
        msg = msg + res.city + "<br/>"
    return HttpResponse(msg)


def updatedata(request):
    obj = Student.objects.get(rollno="R1001")
    obj.name = "Dilanka Harshani"
    obj.address = 'LK 002'
    obj.city = 'Negombo'
    obj.save()
    msg = "Record Updated"
    return HttpResponse(msg)


def deletedata(request):
    obj = Student.objects.get(rollno="R1001")
    obj.delete()
    msg = "Record deleted"
    return HttpResponse(msg)
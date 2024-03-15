from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . import models

def Home(request):
    template = loader.get_template('Home.html')

    return HttpResponse(template.render())


def Application(request):
    template = loader.get_template('Application.html')
    template2 = loader.get_template('details.html')

    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Age = request.POST['Age']
        DOB = request.POST['DOB']

        if int(Age) <= 0:
            context = {
                'error': "Enter Correct Age"
            }
            return HttpResponse(template.render(context,request))
        if models.Application.objects.filter(Email = Email):
            context = {
                'error':"Email ID Already Exist"
            }
            return HttpResponse(template.render(context,request))
        

        details = models.Application(Name = Name, Email = Email, Age = Age, DateOfBirth = DOB)
        details.save()
        return redirect('details')
    return render(request, "Application.html")


def details(request):
    template = loader.get_template('details.html')
    data = models.Application.objects.all().values()

    context = {
        'data': data
    }
    return HttpResponse(template.render(context,request))
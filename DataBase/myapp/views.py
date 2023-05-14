from .models import Student
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, request
from django.views.generic.edit import CreateView


def get_data(request):

    myData = Student.objects.all().values()
    context={'myData':myData}

    return render(request, 'showData.html', context)



def index(request):

    return render(request, 'show.html')


class StudentCreate(CreateView):
    model = Student
    fields= ['fName','lName']
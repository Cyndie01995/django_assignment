from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


# Create your views here.
# def stu(request):
#     return HttpResponse('my first project ever')

def stu(request):
  template = loader.get_template('myfile.html')
  return HttpResponse(template.render())
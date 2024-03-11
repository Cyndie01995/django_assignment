from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Lecturer
# Create your views here.


# Create your views here.
# def stu(request):
#     return HttpResponse('my first project ever')

# def stu(request):
#   template = loader.get_template('lec.html')
#   return HttpResponse(template.render())

def stu(request):
    all_posts = Lecturer.objects.all()
    con = {
        'all_posts': all_posts
    }
    return render(request, 'lecturers/lec.html', con)
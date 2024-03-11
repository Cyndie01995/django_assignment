from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# def get_info(request):
    # return HttpResponse('I love to have pizza and cookies')

def stu(request):
    all_posts = Student.objects.all()
    san = {
        'all_posts': all_posts
    }
    return render(request, 'students_unn/stu.html', san)
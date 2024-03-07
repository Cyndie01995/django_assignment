
from django.urls import path
from .views import *

urlpatterns = [
    path('class/', stu, name= 'members' )
]

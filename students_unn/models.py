from django.db import models
from django.contrib.auth.models import User
# from django.db.models import UserManager
from django.utils import timezone


# Create your models here.
class UndergraduateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Student.Status.UNDERGRADUATE)

class Student(models.Model):
    
    class Status(models.TextChoices):
        UNDERGRADUATE = 'UG', 'UNDERGRADUATE'
        POSTGRADUATE = 'PG', 'POSTGRADUATE'
        SANDWICH = 'SD', 'SANDWICH'
        
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    reg_no = models.PositiveIntegerField()
    dept = models.CharField(max_length=100)
    level = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.UNDERGRADUATE)
    undergraduate = UndergraduateManager()
    objects = models.Manager()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
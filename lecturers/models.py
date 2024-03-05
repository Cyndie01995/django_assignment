from django.db import models

# Create your models here.
class Lecturer(models.Model):
    
    class Status(models.TextChoices):
        LECTURER = 'LC', 'LECTURER'
        DOCTORATE = 'DO', 'DOCTORATE'
        PROFESSOR = 'PF', 'PROFESSOR'
        
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    qualifications = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.LECTURER)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    


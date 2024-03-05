from django.contrib import admin
from .models import Student

# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','reg_no', 'dept', 'level', 'created_at','status')


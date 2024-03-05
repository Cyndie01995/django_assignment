from django.contrib import admin
from .models import Lecturer

# Register your models here.
# admin.site.register(Lecturer)
@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'faculty', 'qualifications', 'created_at','status')


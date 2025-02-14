from django.contrib import admin
from .models import Student
from .models import Teacher
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollnumber','city','marks','passing_date']



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','empnum','city','salary','join_date']
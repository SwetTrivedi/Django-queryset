from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    # student_data=Student.objects.all()

    # student_data=Student.objects.filter(marks=90)

    # student_data=Student.objects.exclude(marks=90)

    # student_data=Student.objects.order_by('city')

    # student_data=Student.objects.order_by('id').reverse()[:2]

    student_data=Student.objects.values()
    student_data=Student.objects.values("name",'city')
    
    print("Return :",student_data)
    print("sql :",student_data.query )
    return render(request,'home.html',{'student':student_data})


























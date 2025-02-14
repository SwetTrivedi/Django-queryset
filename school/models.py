from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    rollnumber=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=70)
    marks=models.IntegerField()
    passing_date=models.DateField()



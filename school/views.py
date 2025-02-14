from django.shortcuts import render
from .models import Student
from .models import Teacher
# Create your views here.
def home(request):
    student_data=Student.objects.all()
    a=type(student_data)
    print(a)
    # student_data=Student.objects.filter(marks=90)

    # student_data=Student.objects.exclude(marks=90)

    # student_data=Student.objects.order_by('city')

    # student_data=Student.objects.order_by('id').reverse()[:2]

    # student_data=Student.objects.values()
    # student_data=Student.objects.values("name",'city')
    

    # student_data=Student.objects.values_list()
    # student_data=Student.objects.values_list('id','name',named=True)

    # student_data=Student.objects.dates('passing_date','month')
    print("Return :",student_data)
    print("sql :",student_data.query )
    return render(request,'home.html',{'student':student_data})



    ############################################################################################################


    ######### Second table 'Teacher' started ############
    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs2.union(qs1,all=True)


    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs2.intersection(qs1)

    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs2.difference(qs1)


    # print("Return :",student_data)
    # print("sql :",student_data.query )
    # return render(request,'home.html',{'student':student_data})





######################################################################################################################



#########################  AND opreator #######################

    # student_data=Student.objects.filter(id=4) & Student.objects.filter(rollnumber=104)

    # print("Return :",student_data)
    # print("sql :",student_data.query )
    # return render(request,'home.html',{'student':student_data})

    # student_data=Student.objects.filter(id=4) | Student.objects.filter(rollnumber=105)

    # print("Return :",student_data)
    # print("sql :",student_data.query )
    # return render(request,'home.html',{'student':student_data})




###############################################################################################################################

# def home(request):
    # student_data=Student.objects.get(pk=1)

    # student_data=Student.objects.first()
    # student_data=Student.objects.order_by('name').first()

    # student_data=Student.objects.last()

    # student_data=Student.objects.latest('passing_date')

    #student_data=Student.objects.earliest('passing_date')

    # student_data=Student.objects.all()
    # print(student_data.exists())

    # student_data=Student.objects.create(name='sameer',rollnumber='107',city='Meerut',marks='70',passing_date='2024-5-4')

    # student_data,created=Student.objects.get_or_create(name='sameer',rollnumber='107',city='Meerut',marks='70',passing_date='2024-5-4')
    # print(created)


    # student_data=Student.objects.filter(id=6).update(name='kabir',marks=80)


    # student_data=Student.objects.filter(marks=70).update(city='pass')


    # student_data,created=Student.objects.update_or_create(id=5,name='vikash',defaults={'name':'vikky'})
    # print(created)



    # objs=[
    #     Student(name="Kunal",rollnumber=108,city="lucknow",marks=82,passing_date='2024-4-5'),
    #     Student(name="shivay",rollnumber=109,city="Mumbai",marks=72,passing_date='2025-6-9'),
    #     Student(name="prince",rollnumber=110,city="Kolkata",marks=92,passing_date='2024-7-10',)
    # ]
    # student_data=Student.objects.bulk_create(objs)



    # all_student_data=Student.objects.all()
    # for stu in all_student_data:
    #     stu.city='Lucknow'
    #     student_data=Student.objects.bulk_update(all_student_data,['city'])



    # student_data=Student.objects.in_bulk([1,2])
    # print(student_data[1].name)


    # student_data=Student.objects.get(pk=10).delete()
    # student_data=Student.objects.filter(marks=70).delete()

    # print("Return :",student_data)
    # return render(request,'home.html',{'student':student_data})

















































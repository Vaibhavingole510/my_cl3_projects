
from django.shortcuts import render
from .models import StudentInformation, Attendance, Activity, Account

def student_list(request):
    students = StudentInformation.objects.all()
    return render(request, 'mis/student_list.html', {'students': students})

def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'mis/attendance_list.html', {'attendance': attendance})

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'mis/activity_list.html', {'activities': activities})

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'mis/account_list.html', {'accounts': accounts})

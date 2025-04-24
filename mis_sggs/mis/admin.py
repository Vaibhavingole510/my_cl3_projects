from django.contrib import admin
from .models import StudentInformation, Attendance, Activity, Account

admin.site.register(StudentInformation)
admin.site.register(Attendance)
admin.site.register(Activity)
admin.site.register(Account)

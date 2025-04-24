from django.urls import path
from . import views  # Import the views we created earlier

urlpatterns = [
    path('students/', views.student_list, name='student_list'),  # URL for the student list
    path('attendance/', views.attendance_list, name='attendance_list'),  # URL for attendance
    path('activities/', views.activity_list, name='activity_list'),  # URL for activities
    path('accounts/', views.account_list, name='account_list'),  # URL for accounts
]

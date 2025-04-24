
from django.db import models

class StudentInformation(models.Model):
    reg_no = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()
    address = models.TextField()
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    reg_no = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    date = models.DateField()
    subject = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=[('Theory', 'Theory'), ('Practical', 'Practical')])
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.reg_no} - {self.date}"

class Activity(models.Model):
    reg_no = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    name_of_activity = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=100)
    prize = models.CharField(max_length=100, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name_of_activity

class Account(models.Model):
    reg_no = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    fees_type = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.reg_no} - {self.fees_type}"

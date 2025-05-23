# Generated by Django 5.1.4 on 2025-01-08 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Theory', 'Theory'), ('Practical', 'Practical')], max_length=20)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=20)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.studentinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_activity', models.CharField(max_length=100)),
                ('organization_name', models.CharField(max_length=100)),
                ('prize', models.CharField(blank=True, max_length=100)),
                ('date', models.DateField()),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.studentinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_type', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.studentinformation')),
            ],
        ),
    ]

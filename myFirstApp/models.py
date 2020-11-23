from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    # this will create table Student automatically
    # Student Class models will be mapped to this table
    class Meta:
        db_table = "Student"
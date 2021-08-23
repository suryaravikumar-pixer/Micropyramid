from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    # class Meta:
    #     db_table='student_info'
        
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    college=models.CharField(max_length=100)
    city=models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

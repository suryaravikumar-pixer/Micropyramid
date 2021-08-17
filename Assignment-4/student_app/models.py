from django.db import models
from django.urls import reverse
"""A OneToOneField is essentially the same as a ForeignKey, with the exception that always carries a "unique" constraint 
with it and the reverse relation always returns the object pointed to (since there will only ever be one), rather 
than returning a list."""

# Create your models here.
class Department(models.Model):
    branch = models.CharField(max_length=100) #Lecturer as a string rather than object because it's been declared in the file after this class
    # lecturer=models.ManyToManyField('Lecturer')  
    # student =  models.ManyToManyField('Student')


    def __str__(self):
        return self.branch
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email=  models.EmailField(unique=True)
    department= models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name

    # def get_absolute_url(self):
    #     return reverse('student_detail', args=[str(self.id)])




class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    # student=models.ManyToManyField(Student)
    department=models.ManyToManyField(Department)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('student_update', args=[int(self.id)])




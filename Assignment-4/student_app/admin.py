from django.contrib import admin
from .models import Lecturer, Student, Department
# Register your models here.

admin.site.register([Lecturer, Student, Department])

from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from student_app.models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

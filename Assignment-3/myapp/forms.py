from django import forms
from django.forms.models import model_to_dict
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


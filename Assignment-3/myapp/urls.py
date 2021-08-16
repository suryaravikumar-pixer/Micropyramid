from myapp.forms import StudentForm
from django.urls import path
from . views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('createview',CreateStudent.as_view(), name='add_student'),
    path('update/<int:pk>/', UpdateStudent.as_view(), name='edit_stu'),
    path('delete/<int:pk>/', DeleteStudent.as_view(), name='del_stu'),
]
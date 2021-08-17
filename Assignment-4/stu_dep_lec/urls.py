
from django.contrib import admin
from django.urls import path
from django.views.generic.base import View
from student_app.views import SearchStudent, StudentCreateView
from student_app.views import StudentUpdateView
from student_app.views import StudentListView
# from student_app.views import 
# from . import views  # StudentCreateView, student_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/',StudentListView.as_view(), name='student_detail'),
    path('csd/',StudentCreateView.as_view()),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('search_student/<int:pk>/', SearchStudent.as_view(), name='search_student'),
]

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
# from django.views.generic.detail import DetailView
from .models import Student
from .forms import StudentForm
class IndexView(ListView):
    model=Student
    template_name='myapp/list_view.html'
    context_object_name='index_stu_list'
   

# class StudentDetail(DetailView):
#     model=Student
#     template_name='myapp/detail_view.html'
#     context_object_name='student-detail'

class CreateStudent(CreateView):
    model=Student
    form_class=StudentForm
    template_name='myapp/create_view.html'
    success_url='/'

class UpdateStudent(UpdateView):
    model=Student
    fields='__all__'
    template_name='myapp/update_view.html'
    success_url='/'

class DeleteStudent(DeleteView):
    model=Student
    template_name='myapp/delete_view.html'
    success_url='/'

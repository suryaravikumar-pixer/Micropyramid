from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Student, Department, Lecturer
from django.db.models import Q
from .forms import StudentCreateForm

from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView

class StudentListView(ListView):
    model=Student
    template_name='student_app/base.html'


class StudentCreateView(CreateView):
	template_name='student_app/student_create.html'
	form_class = StudentCreateForm

def student_create(request, id):
    return HttpResponse("<h1>Successfully crated student derails</h1>")

class StudentUpdateView(UpdateView):
    model=Student
    fields='__all__'
    # form_class=StudentCreateForm
    template_name='student_app/student_update.html'
    success_url='student_detail'

    # def get_object(self):
    #     return get_object_or_404(Student.name, pk=request.session['user_id'])

# def student_update(request, id):
#     return HttpResponse("<h1>updated</h1>")
class SearchStudent(DetailView):
	model= Student
	# context_object_name = 'results'
	template_name='student_app/student_search.html'
	def get_queryset(self):
		query = self.request.GET.get('q')
        
		return Student.objects.filter(Q(name__icontains=query)| Q(email__icontains=query))
from django.views.generic import ListView
from django.views.generic.edit import CreateView,FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Student, Teacher
from .models import StudentForm, TeacherForm
# Create your views here.

class StudentList(ListView):
     model = Student

class TeacherList(ListView):
     model = Teacher

class StudentCreate(CreateView):
      model = Student
      fields = ['name','birth_date','dre','course']

class StudentUpdate(UpdateView):
      model = Student
      fields = ['name','birth_date','dre','course']

class StudentDelete(DeleteView):
      model = Student
      success_url = reverse_lazy('student-list')

class TeacherCreate(CreateView):
      model = Teacher
      fields = ['name','birth_date','department']

class TeacherUpdate(UpdateView):
      model = Teacher
      fields = ['name','birth_date','department']

class TeacherDelete(DeleteView):
      model = Teacher
      success_url = reverse_lazy('teacher-list')

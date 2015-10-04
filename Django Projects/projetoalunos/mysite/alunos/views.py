from django.views.generic.base import TemplateView
import datetime
from django.forms.widgets import TextInput
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import ListView
from django.views.generic.edit import CreateView,FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .forms import StudentForm,StudentUpdateForm
from .models import Student,Orientador, studentFieldsList,orientadorFieldsList
from mysite import settings
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"
	
class StudentList(ListView):
     model = Student

"""class StudentCreate(CreateView):
    model = Student
    fields = studentFieldsList
    sucess_url = reverse_lazy('student-list')"""
class StudentCreate(CreateView):
    form_class = StudentForm
    template_name = 'student_form.html'
    sucess_url = reverse_lazy('student-list')
    
"""	  
      def form_valid(self,form):
            if (Student.dre_valid()):
                return super(StudentCreate,self).form_valid(form)

"""
"""
class StudentUpdate(UpdateView):
    model = Student
    fields = studentFieldsList
    sucess_url = reverse_lazy('student-list')
"""
class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'student_form.html'
    sucess_url = reverse_lazy('student-list')
    
class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')                
        
class OrientadorList(ListView):
     model = Orientador	

class OrientadorCreate(CreateView):
    model = Orientador
    fields = orientadorFieldsList
    sucess_url = reverse_lazy('orientador-list')
"""	  
      def form_valid(self,form):
            if (Orientador.dre_valid()):
                return super(OrientadorCreate,self).form_valid(form)

"""
class OrientadorUpdate(UpdateView):
    model = Orientador
    fields = orientadorFieldsList
    sucess_url = reverse_lazy('orientador-list')
        
class OrientadorDelete(DeleteView):
    model = Orientador
    success_url = reverse_lazy('orientador-list')        
        
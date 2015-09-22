from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView,FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Student,StudentUser,TeacherUser, studentFieldsList,studentUserFieldsList,teacherFieldsList
from django.contrib.auth.models import User
from django import forms
from forms import StudentAddForm, StudentUserCreationForm,TeacherUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from mysite import settings
from .backends.studentbackend import  StudentBackend
# Create your views here.

class HomePageView(TemplateView):
	template_name = "base.html"
	
class StudentList(ListView):
     model = Student	

class StudentUserList(ListView):
     model = StudentUser

class TeacherUserList(ListView):
    model = TeacherUser


class StudentUserUpdate(UpdateView):
    model = StudentUser
    fields = studentUserFieldsList
    sucess_url = reverse_lazy('student-list')

class StudentUserDelete(DeleteView):
      model = StudentUser
      success_url = reverse_lazy('student-list')

class TeacherUserUpdate(UpdateView):
      model = TeacherUser
      fields = ['name','birth_date','department']
      success_url = reverse_lazy('teacher-list')

class TeacherUserDelete(DeleteView):
    model = TeacherUser
    success_url = reverse_lazy('teacher-list')

class StudentCreate(CreateView):
      model = Student
      fields = studentFieldsList
      sucess_url = reverse_lazy('studentuser-list')
"""	  
      def form_valid(self,form):
            if (Student.dre_valid()):
                return super(StudentCreate,self).form_valid(form)

"""
class StudentUpdate(UpdateView):
      model = Student
      fields = studentFieldsList
      sucess_url = reverse_lazy('student-list')
        
class StudentDelete(DeleteView):
      model = Student
      success_url = reverse_lazy('student-list')        
        
    
def StudentAddUser(request):
    if request.method == "POST":
        form = StudentAddForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            # redirect, or however you want to get to the main view
            return reverse_lazy('student-list')
    else:
        form = StudentAddForm() 

    return render(request, 'adduser.html', {'form': form}) 

def StudentCreateUser(request):
    if request.method == "POST":
        form = StudentUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
	    user.set_password(user.password)
	    user.save()
        
        backend = StudentBackend()
        if (backend.authenticate(username=username, password=password))!=None:
            login(request,user)
            # redirect, or however you want to get to the main view
        return reverse_lazy('student-list')
    else:
        form = StudentUserCreationForm()

    return render(request, 'createuser.html', {'form': form})
"""
def StudentUserLogin(request):
#    if request.method == "POST":
        form = AuthenticationForm(None,request.POST)
        if form.is_valid():
            login(request,auth_form.get_user())
            return HttpResponseRedirect('/home/')
        return render(request,'login.html',{'form':form})    
            
"""    
def StudentUserLogin(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.


    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        backend = StudentBackend()
        user = backend.authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('studentuser-list')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)
    
@login_required
def StudentUserLogout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/home/')

    
        
    
def TeacherAddUser(request):
    if request.method == "POST":
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            # redirect, or however you want to get to the main view
            return reverse_lazy('teacher-list')
    else:
        form = TeacherAddForm() 

    return render(request, 'adduser.html', {'form': form}) 

def TeacherCreateUser(request):
    if request.method == "POST":
        form = TeacherUserCreationForm(request.POST)
        if form.is_valid():
#            new_user = User.objects.create_user(TeacherUser.self,TeacherUser.name,TeacherUser.birth_date,TeacherUser.department)
 	   user = form.save()
	   user.set_password(user.password)
	   user.save()
           login(request,user)
            # redirect, or however you want to get to the main view
           return reverse_lazy('teacher-list')
    else:
        form = TeacherUserCreationForm()

    return render(request, 'createuser.html', {'form': form})

def TeacherUserLogin(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.





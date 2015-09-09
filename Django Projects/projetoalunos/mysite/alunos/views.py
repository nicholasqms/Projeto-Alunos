from django.views.generic import ListView
from django.views.generic.edit import CreateView,FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Student, Teacher, Grade
from .models import StudentForm, TeacherForm
from django.contrib.auth.models import User
from django import forms
from forms import StudentAddForm, StudentUserCreationForm
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
# Create your views here.

class StudentList(ListView):
     model = Student

class TeacherList(ListView):
     model = Teacher

class StudentCreate(CreateView):
      model = Student
      fields = ['name','birth_date','dre','course']
      sucess_url = reverse_lazy('student-list')

class StudentUpdate(UpdateView):
      model = Student
      fields = ['name','birth_date','dre','course']
      sucess_url = reverse_lazy('student-list')

class StudentDelete(DeleteView):
      model = Student
      success_url = reverse_lazy('student-list')

class TeacherCreate(CreateView):
      model = Teacher
      fields = ['name','birth_date','department']
      success_url = reverse_lazy('teacher-list')

class TeacherUpdate(UpdateView):
      model = Teacher
      fields = ['name','birth_date','department']
      success_url = reverse_lazy('teacher-list')

class TeacherDelete(DeleteView):
      model = Teacher
      success_url = reverse_lazy('teacher-list')

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
#            new_user = User.objects.create_user(StudentUser.self,StudentUser.name,StudentUser.birth_date,StudentUser.dre,StudentUser.course)
 	   user = form.save()
	   user.set_password(user.password)
	   user.save()
           login(request,user)
            # redirect, or however you want to get to the main view
           return reverse_lazy('student-list')
    else:
        form = StudentUserCreationForm()

    return render(request, 'createuser.html', {'form': form})

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
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return reverse_lazy('main')
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
#class UserCreationForm(forms.ModelForm)
#"""
#    A form that creates a user, with no privileges, from the given username and
#    password.
#    """
#    error_messages = {
 #       'password_mismatch': _("The two password fields didn't match."),
 #   }
  #  password1 = forms.CharField(label=_("Password"),
   #     widget=forms.PasswordInput)
    #password2 = forms.CharField(label=_("Password confirmation"),
     #   widget=forms.PasswordInput,
      #  help_text=_("Enter the same password as above, for verification."))

   # class Meta:
#        model = User
 #       fields = ("username",)
#
 #   def clean_password2(self):
  #      password1 = self.cleaned_data.get("password1")
   #     password2 = self.cleaned_data.get("password2")
    #    if password1 and password2 and password1 != password2:
     #       raise forms.ValidationError(
      #          self.error_messages['password_mismatch'],
       #         code='password_mismatch',
   #         )
  #      return password2

 #   def save(self, commit=True):
#        user = super(UserCreationForm, self).save(commit=False)
#        user.set_password(self.cleaned_data["password1"])
#        if commit:
#            user.save()
#        return user





from django.views.generic import ListView
from django.views.generic.edit import CreateView,FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Student, Teacher, Grade
from .models import StudentForm, TeacherForm
from django.contrib.auth.models import User
from django import forms
from forms import StudentAddForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
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





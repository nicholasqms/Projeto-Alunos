import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.auth.models import Group
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import TextInput
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Student,Orientador, studentFieldsList,orientadorFieldsList
#cfrom captcha.fields import CaptchaField

class StudentForm(ModelForm): 
#    data_Nascimento = forms.DateField(blank=True, null= False, required = True, widget= SelectDateWidget)
    class Meta:
        model = Student
        fields = studentFieldsList        
        required = studentFieldsList
        widgets = {'data_Nascimento' : forms.DateInput(attrs={'type':'date'}), 'DRE': TextInput,                 
                   'RG': TextInput, 'rg_validade' : forms.DateInput(attrs={'type':'date'}),'passaporte_numero' : TextInput,
                   'CEP': TextInput , 'telefone': TextInput , 
                   'passaporte_validade' : forms.DateInput(attrs={'type':'date'}),
                   'numero_agencia' : TextInput, 'numero_conta' : TextInput
                  }
        
class StudentUpdateForm(StudentForm):
    class Meta:
        model = Student
        fields = studentFieldsList        
        required = studentFieldsList
        widgets = {'data_Nascimento' : forms.DateInput(attrs={'type':'date'}), 'DRE': TextInput,                 
                   'RG': TextInput, 'rg_validade' : forms.DateInput(attrs={'type':'date'}),'passaporte_numero' : TextInput,
                   'CEP': TextInput , 'telefone': TextInput , 
                   'passaporte_validade' : forms.DateInput(attrs={'type':'date'}),
                   'numero_agencia' : TextInput, 'numero_conta' : TextInput
                  }
        
        exclude = ('user',)
"""
class StudentUserCreationForm(forms.ModelForm):
#    A form for creating new users. Includes all the required
#    fields, plus a repeated password.
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = StudentUser
        fields = studentUserFieldsList
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StudentUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class StudentUserChangeForm(forms.ModelForm):
    """#A form for updating users. Includes all the fields on
#    the user, but replaces the password field with admin's
#    password hash display field.
#    """
#    password = ReadOnlyPasswordHashField()
#
"""   class Meta:
        model = StudentUser
        fields = studentUserFieldsList
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class OrientadorCreationForm(forms.ModelForm):
    """#A form for creating new users. Includes all the required
   # fields, plus a repeated password."""
"""    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Orientador
        fields = teacherFieldsList

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(OrientadorCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class OrientadorChangeForm(forms.ModelForm):
#"""# A form for updating users. Includes all the fields on
#    the user, but replaces the password field with admin's
#    password hash display field.
"""password = ReadOnlyPasswordHashField()

    class Meta:
        model = Orientador
        fields = teacherFieldsList

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"] """

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

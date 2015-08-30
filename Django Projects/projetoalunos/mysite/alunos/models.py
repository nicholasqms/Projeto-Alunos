import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=100)
    	birth_date = models.DateField(blank=True, null=True)
	dre = models.PositiveIntegerField(blank=True, null= True)
	course = models.CharField(max_length=100)
    	def __str__(self):              # __unicode__ on Python 2
        	return self.name
	def get_absolute_url(self):
            return reverse('student-detail', kwargs={'pk': self.pk})

class Teacher(models.Model):
	name = models.CharField(max_length=100)
	birth_date = models.DateField(blank=True, null=True)
	department = models.CharField(max_length=50)
	
        def __str__(self):              # __unicode__ on Python 2
                return self.name
	def get_absolute_url(self):
            return reverse('teacher-detail', kwargs={'pk': self.pk})

class StudentForm(ModelForm):
	class Meta:
	  model = Student
	  fields = ['name','birth_date','dre','course']

class TeacherForm(ModelForm):
	class Meta:
	  model = Teacher
	  fields = ['name','birth_date','department']

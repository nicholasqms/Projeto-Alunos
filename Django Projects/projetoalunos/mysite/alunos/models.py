import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
# Create your models here.

class Student(models.Model):
#3	user = models.OneToOneField(User);
	name = models.CharField(max_length=100)
    	birth_date = models.DateField(blank=True, null=True)
	dre = models.PositiveIntegerField(blank=True, null= True)
	course = models.CharField(max_length=100)
    	def __str__(self):              # __unicode__ on Python 2
        	return self.name
	def get_absolute_url(self):
            return reverse('student', kwargs={'pk': self.pk})

class Grade(models.Model):
	subject= models.CharField(max_length=100)
	student = models.ForeignKey(Student)
	student_grade = models.DecimalField(max_digits=4, decimal_places=2)
    	def __str__(self):              # __unicode__ on Python 2
        	return self.subject
	def get_absolute_url(self):
            return reverse('grade', kwargs={'pk': self.pk})

class Teacher(models.Model):
	name = models.CharField(max_length=100)
	birth_date = models.DateField(blank=True, null=True)
	department = models.CharField(max_length=50)
	
        def __str__(self):              # __unicode__ on Python 2
                return self.name
	def get_absolute_url(self):
            return reverse('teacher', kwargs={'pk': self.pk})

class StudentForm(ModelForm):
	class Meta:
	  model = Student
	  fields = ['name','birth_date','dre','course']

class TeacherForm(ModelForm):
	class Meta:
	  model = Teacher
	  fields = ['name','birth_date','department']

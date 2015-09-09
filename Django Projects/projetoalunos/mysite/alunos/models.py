import datetime
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
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
            return reverse('student-list')
#	pk = self.pk
#            return reverse('student-list', kwargs={'pk': self.pk})

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
            return reverse('teacher-list', kwargs={'pk': self.pk})

class StudentForm(ModelForm):
	class Meta:
	  model = Student
	  fields = ['name','birth_date','dre','course']

class TeacherForm(ModelForm):
	class Meta:
	  model = Teacher
	  fields = ['name','birth_date','department']


class StudentUser(AbstractBaseUser):
    name = models.CharField(
        verbose_name='Student\'s Name',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    birth_date = models.DateField(blank=True, null=True)
    dre = models.PositiveIntegerField(blank=True, null= True)
    course = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
                return self.name
    def get_absolute_url(self):
            return reverse('student-list')
#            return reverse('student-list', kwargs={'pk': self.pk})


#    objects = MyUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['birth_date','dre','course']

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

#    def get_short_name(self):
        # The user is identified by their email address
#        return self.email

 #   def __str__(self):              # __unicode__ on Python 2
  #      return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        #return self.is_admin
	return False



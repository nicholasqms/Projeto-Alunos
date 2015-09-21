import datetime
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

studentInactiveStatusList = ['Graduado','Trancado','Transferencia']
studentFieldsList = ['name','bolsa','tipo','birth_date','dre','rg','zip_code','residence_address','telephone_number','course']
teacherFieldsList = ['name','birth_date','register_number','CPF','contact','email']
tipoBolsa = [('PIBIC','PIBIC'),('FAPERJ','FAPERJ'),('CNPq','CNPq'),('Projeto','Projeto')]
tipoOrientado = [('Ensino Medio','Ensino Medio'),('Iniciacao Cientifica','Iniciacao Cientifica'),('Mestrado','Mestrado'),('Doutorado','Doutorado')]
tipoOrientador = ['Professor','Pesquisador']

# Create your models here.




class Student(models.Model):
    user =models.OneToOneField(User)
    name = models.CharField(
        verbose_name='Student\'s Name',
        max_length=255
    )
    bolsa = models.CharField(max_length=7, choices = tipoBolsa,default='PIBIC')
    tipo = models.CharField(max_length=30, choices = tipoOrientado,default='Iniciacao Cientifica')
    birth_date = models.DateField(blank=True, null=True)
    dre = models.PositiveIntegerField(blank=True, null= True)
    rg = models.PositiveIntegerField(blank=True, null=True)
    zip_code = models.PositiveIntegerField(blank=True, null=True)
    residence_address = models.CharField(max_length=255, default = 'Insira o endereco de residencia')
    telephone_number = models.PositiveIntegerField(blank=True, null=True)
    course = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def get_absolute_url(self):
        return reverse('student-list')
#	pk = self.pk
#            return reverse('student-list', kwargs={'pk': self.pk})

class Orientador(models.Model):
    user =models.OneToOneField(User)
    name = models.CharField(
        verbose_name='Nome do Orientador',
        max_length=255
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    birth_date = models.DateField(blank=True, null=True)
    register_number = models.PositiveIntegerField(blank=True, null = True)
    email = models.CharField(max_length=100, default='your_email@service.com')
    contact = models.PositiveIntegerField(blank=True, null = True)
    CPF = models.PositiveIntegerField(blank=True, null = True)


class StudentUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='Username',
        max_length=30,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Student\'s Name',
        max_length=255
    )
    tipo = models.CharField(max_length=30, choices = tipoOrientado,default='Iniciacao Cientifica')
    bolsa = models.CharField(max_length=7, choices = tipoBolsa,default='PIBIC')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    birth_date = models.DateField(blank=True, null=True)
    dre = models.PositiveIntegerField(blank=True, null= True)
    rg = models.PositiveIntegerField(blank=True, null=True)
    zip_code = models.PositiveIntegerField(blank=True, null=True)
    residence_address = models.CharField(max_length=255, default = 'Insira o endereco de residencia')
    telephone_number = models.PositiveIntegerField(blank=True, null=True)
    course = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
                return self.name
    def get_absolute_url(self):
            return reverse_lazy('studentuser-list')
#            return reverse('student-list', kwargs={'pk': self.pk})


#    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = studentFieldsList

    def get_full_name(self):
        # The user is identified by their name
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

class TeacherUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='Username',
        max_length=30,
        unique=True
    )
    name = models.CharField(
        verbose_name='Teacher\'s Name',
        max_length=255
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    birth_date = models.DateField(blank=True, null=True)
    register_number = models.PositiveIntegerField(blank=True, null = True)
    email = models.CharField(max_length=100, default='your_email@service.com')
    contact = models.PositiveIntegerField(blank=True, null = True)
    CPF = models.PositiveIntegerField(blank=True, null = True)
    
    
    
    def __str__(self):              # __unicode__ on Python 2
                return self.name
    def get_absolute_url(self):
            return reverse('teacheruser-list')
#            return reverse('student-list', kwargs={'pk': self.pk})


#    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = teacherFieldsList

    def get_full_name(self):
        # The user is identified by their name
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

					 					 					 


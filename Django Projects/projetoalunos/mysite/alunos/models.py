import datetime
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ValidationError
#from alunos.validators import dre_is_valid

studentStatusList = [('Ativo','Ativo'),('Inativo','Inativo'),('Viajando','Viajando')]
studentInactiveStatusList = ['Graduado','Trancado','Transferencia']
studentFieldsList = ['user','name','bolsa','tipo','status','data_Nascimento','DRE','RG','CEP','endereco','telefone','curso','orientador_aluno']
orientadorFieldsList = ['user','name','is_active','is_admin','data_Nascimento','CPF','email','contato','numero_Registro']
tipoBolsa = [('PIBIC','PIBIC'),('FAPERJ','FAPERJ'),('CNPq','CNPq'),('Projeto','Projeto')]
tipoOrientado = [('Ensino Medio','Ensino Medio'),('Iniciacao Cientifica','Iniciacao Cientifica'),('Mestrado','Mestrado'),('Doutorado','Doutorado')]
tipoOrientador = ['Professor','Pesquisador']

# Create your models here.



class Student(models.Model):
    user =models.OneToOneField(User)
    name = models.CharField(
        verbose_name='Nome do Aluno',
        max_length=255
    )
    studentFieldsList = ['user','name','bolsa','tipo','data_Nascimento','DRE','RG','CEP','endereco','telefone','curso']
    bolsa = models.CharField(max_length=7, choices = tipoBolsa,default='PIBIC')
    tipo = models.CharField(max_length=30, choices = tipoOrientado,default='Iniciacao Cientifica')
    data_Nascimento = models.DateField(blank=True, null=True)
    DRE = models.PositiveIntegerField(blank=True, null= True)#,validators=[dre_is_valid])
    RG = models.PositiveIntegerField(blank=True, null=True)
    CEP = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=255, default = 'Insira o endereco de residencia')
    telefone = models.PositiveIntegerField(blank=True, null=True)
    curso = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices =studentStatusList ,default='Ativo')
    orientador_aluno = models.ForeignKey('Orientador',verbose_name="Orientador")
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def get_absolute_url(self):
        return reverse('student-list')
#	pk = self.pk
#            return reverse('student-list', kwaRGs={'pk': self.pk})

class Orientador(models.Model):
    user =models.OneToOneField(User)
    name = models.CharField(
        verbose_name='Nome do Orientador',
        max_length=255
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    data_Nascimento = models.DateField(blank=True, null=True)
    numero_Registro = models.PositiveIntegerField(blank=True, null = True)
    email = models.CharField(max_length=100, default='your_email@service.com')
    contato = models.PositiveIntegerField(blank=True, null = True)
    CPF = models.PositiveIntegerField(blank=True, null = True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def get_absolute_url(self):
        return reverse('student-list')
    
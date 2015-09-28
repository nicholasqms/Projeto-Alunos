# -*- coding: utf-8 -*-
import datetime
from django.forms.extras.widgets import SelectDateWidget
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
studentFieldsList = ['user','email','name','bolsa','tipo','status','data_Nascimento','DRE','RG','CEP','endereco','telefone','curso','passaporte_numero','passaporte_validade','orientador_aluno']
orientadorFieldsList = ['user','name','is_active','is_admin','data_Nascimento','CPF','email','contato','numero_Registro']
tipoBolsa = [('PIBIC','PIBIC'),('FAPERJ','FAPERJ'),('CNPq','CNPq'),('Projeto','Projeto')]
tipoOrientado = [('Ensino Medio','Ensino Medio'),('Iniciacao Cientifica','Iniciacao Cientifica'),('Mestrado','Mestrado'),('Doutorado','Doutorado')]
tipoOrientador = ['Professor','Pesquisador']

# Create your models here.
def dre_is_valid(value):
    indice = soma = 0
    for indice in range (0,8):
        soma = soma + (value[indice] * (indice + 1))
        if ((soma % 10) != value[indice]):
            raise ValidationError('%s nao e um dre valido' %value)

def my_validator(value):
    if (value != 114032011):
        raise ValidationError('%s não é um dre valido' %value)  


class StudentStatus(models.Model):
    name = models.CharField(verbose_name='Status do Aluno',max_length = 255,default='Ativo')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def get_absolute_url(self):
        return reverse('student-list')

class StudentBolsa(models.Model):
    name = models.CharField(verbose_name='Tipo de Bolsa',max_length = 255,default='PIBIC')
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def get_absolute_url(self):
        return reverse('student-list')


class Student(models.Model):
#    tipo_usuario = models.ForeignKey('
    user =models.OneToOneField(User)
    name = models.CharField(
        verbose_name='Nome do Aluno',
        max_length=255
    )
    email = models.EmailField(max_length=254,default = "example@lps.ufrj.br")
    studentFieldsList = ['user','name','email','bolsa','tipo','data_Nascimento','DRE','RG','CEP','endereco','telefone','curso']
    bolsa = models.ForeignKey('StudentBolsa',verbose_name = 'Bolsa')
    tipo = models.CharField(max_length=30, choices = tipoOrientado,default='Iniciacao Cientifica')
    data_Nascimento = models.DateField(blank=True, null=False, default = '2001-01-01')#, widget=SelectDateWidget)
    DRE = models.PositiveIntegerField(blank=True, null= True,validators=[my_validator])
    RG = models.PositiveIntegerField(blank=True, null=True)
    CEP = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=255, default = 'Insira o endereco de residencia')
    telefone = models.PositiveIntegerField(blank=True, null=True)
    curso = models.CharField(max_length=100)
    passaporte_numero = models.PositiveIntegerField(blank=True, null=True, verbose_name = 'Número do Passaporte')
    passaporte_validade = models.DateField(blank=True,null=True,verbose_name = 'Validade do Passaporte')
    status = models.ForeignKey('StudentStatus',verbose_name="Status do Aluno")
#    status = models.CharField(max_length=30, choices =studentStatusList ,default='Ativo')
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
    
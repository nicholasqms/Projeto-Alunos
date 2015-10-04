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
from .listas import listaPaises
#from alunos.validators import dre_is_valid

studentStatusList = [('Ativo','Ativo'),('Inativo','Inativo'),('Viajando','Viajando')]
studentInactiveStatusList = ['Graduado','Trancado','Transferencia']
studentFieldsList = ['user','email','name','bolsa','tipo','status','data_Nascimento','DRE','RG','rg_orgao_expeditor','rg_estado_expedicao','rg_validade' ,'CEP','endereco','telefone','curso','passaporte_numero','passaporte_validade','passaporte_emissao','numero_agencia','numero_conta','orientador_aluno']
orientadorFieldsList = ['user','name','is_active','is_admin','data_Nascimento','CPF','email','contato','numero_Registro']
tipoBolsa = [('PIBIC','PIBIC'),('FAPERJ','FAPERJ'),('CNPq','CNPq'),('Projeto','Projeto')]
tipoOrientado = [('Ensino Medio','Ensino Medio'),('Iniciacao Cientifica','Iniciacao Cientifica'),('Mestrado','Mestrado'),('Doutorado','Doutorado')]
tipoOrientador = ['Professor','Pesquisador']
listaEstados = [('Acre','AC'),('Alagoas','AL'),('Amapá','AP'),('Amazonas','AM'),('Bahia','BA'),
('Ceará','CE'),('Distrito Federal','DF'),('Espírito Santo','ES'),('Goiás','GO'),
('Maranhão','MA'),('Mato Grosso','MT'),
('Mato Grosso do Sul','MS'),('Minas Gerais','MG'),
('Pará','PA'),('Paraíba','PB'),('Paraná','PR'),('Pernambuco','PE'),
('Piauí','PI'),('Rio de Janeiro','RJ'),
('Rio Grande do Norte','RN'),('Rio Grande do Sul','RS'),
('Rondônia','RO'),('Roraima','RR'),('Santa Catarina','SC'),
('São Paulo','SP'),('Sergipe','SE'),('Tocantins','TO')]

# Create your models here.
def dre_is_valid(value):
    if (len(str(value)) != 9):
        raise ValidationError('%s não é um valor válido, insira um numero correto' %value)  
    indice = soma = 0
    for indice in range(0,8):
        soma += ((int(str(value)[indice]))*(indice+1))
    if ((soma%10) != int(str(value)[indice+1])):
            raise ValidationError('%s não é um dre válido' %value)

def length_validator(value):
    if (len(str(value)) != 9):
        raise ValidationError('%s não é um valor válido, insira um numero correto' %value)  


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
    tipo = models.CharField(max_length=30, choices = tipoOrientado,default='Iniciação Científica')
    data_Nascimento = models.DateField(blank=True, null=False, default = '2001-01-01')#, widget=SelectDateWidget)
    DRE = models.PositiveIntegerField(blank=True, null= True,validators=[dre_is_valid])
    RG = models.PositiveIntegerField(blank=True, null=True)
    rg_orgao_expeditor = models.CharField(max_length=20, default = 'Órgão Expeditor', verbose_name = 'Órgão Expeditor')
    rg_estado_expedicao = models.CharField(max_length=30, choices = listaEstados,default='RJ',verbose_name = 'Estado de Expedição')
    rg_validade = models.DateField(blank=True,null=True,verbose_name = 'Validade do RG')
    CEP = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=255, default = 'Insira o endereço de residência')
    telefone = models.PositiveIntegerField(blank=True, null=True)
    curso = models.CharField(max_length=100)
    passaporte_numero = models.PositiveIntegerField(blank=True, null=True, verbose_name = 'Número do Passaporte')
    passaporte_validade = models.DateField(blank=True,null=True,verbose_name = 'Validade do Passaporte')
    passaporte_emissao = models.CharField(max_length=40, choices = listaPaises,default='BR',verbose_name = 'País de Expedição')
    status = models.ForeignKey('StudentStatus',verbose_name="Status do Aluno")
    numero_agencia=models.PositiveIntegerField(blank=True, null=True, verbose_name = 'Número Agência (Banco do Brasil)')
    numero_conta=models.PositiveIntegerField(blank=True, null=True, verbose_name = 'Número Conta')
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
    
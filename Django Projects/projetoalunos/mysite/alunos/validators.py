# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError

def dre_is_valid(value):
    if (len(str(value)) != 9):
        raise ValidationError('%s não corresponde a um DRE , insira um número de 9 dígitos.' %value)  
    indice = soma = 0
    for indice in range(0,8):
        soma += ((int(str(value)[indice]))*(indice+1))
    if ((soma%10) != int(str(value)[indice+1])):
            raise ValidationError('%s não é um DRE válido.' %value)

def length_validator(value):
    if (len(str(value)) != 9):
        raise ValidationError('%s não corresponde a um DRE , insira um número de 9 dígitos.' %value)  
"""        
def string_validator(value):
    if ((type(value) is ) == False):
        raise ValidationError('%s não foi preenchido corretamente, insira um nome' %value)"""
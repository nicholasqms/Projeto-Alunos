from .models import Student

def dre_is_valid(self):
        indice = soma = 0
        for indice in range (0,8):
            soma +=(Student.DRE[indice] * (indice + 1))
            if ((soma % 10) != Student.DRE[indice]):
                raise ValidationError('%s nao e um dre valido' %Student.DRE)
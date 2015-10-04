# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alunos.models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0049_student_passaporte_emissao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='orgao_expeditor',
            new_name='rg_orgao_expeditor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='estado_expedicao',
        ),
        migrations.AddField(
            model_name='student',
            name='rg_estado_expedicao',
            field=models.CharField(default=b'RJ', max_length=30, verbose_name=b'Estado de Expedi\xc3\xa7\xc3\xa3o', choices=[(b'Acre', b'AC'), (b'Alagoas', b'AL'), (b'Amap\xc3\xa1', b'AP'), (b'Amazonas', b'AM'), (b'Bahia', b'BA'), (b'Cear\xc3\xa1', b'CE'), (b'Distrito Federal', b'DF'), (b'Esp\xc3\xadrito Santo', b'ES'), (b'Goi\xc3\xa1s', b'GO'), (b'Maranh\xc3\xa3o', b'MA'), (b'Mato Grosso', b'MT'), (b'Mato Grosso do Sul', b'MS'), (b'Minas Gerais', b'MG'), (b'Par\xc3\xa1', b'PA'), (b'Para\xc3\xadba', b'PB'), (b'Paran\xc3\xa1', b'PR'), (b'Pernambuco', b'PE'), (b'Piau\xc3\xad', b'PI'), (b'Rio de Janeiro', b'RJ'), (b'Rio Grande do Norte', b'RN'), (b'Rio Grande do Sul', b'RS'), (b'Rond\xc3\xb4nia', b'RO'), (b'Roraima', b'RR'), (b'Santa Catarina', b'SC'), (b'S\xc3\xa3o Paulo', b'SP'), (b'Sergipe', b'SE'), (b'Tocantins', b'TO')]),
        ),
        migrations.AddField(
            model_name='student',
            name='rg_validade',
            field=models.DateField(null=True, verbose_name=b'Validade do RG', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='DRE',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[alunos.models.dre_is_valid]),
        ),
        migrations.AlterField(
            model_name='student',
            name='endereco',
            field=models.CharField(default=b'Insira o endere\xc3\xa7o de resid\xc3\xaancia', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='numero_agencia',
            field=models.PositiveIntegerField(null=True, verbose_name=b'N\xc3\xbamero Ag\xc3\xaancia (Banco do Brasil)', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tipo',
            field=models.CharField(default=b'Inicia\xc3\xa7\xc3\xa3o Cient\xc3\xadfica', max_length=30, choices=[(b'Ensino Medio', b'Ensino Medio'), (b'Iniciacao Cientifica', b'Iniciacao Cientifica'), (b'Mestrado', b'Mestrado'), (b'Doutorado', b'Doutorado')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0042_student_passaporte_validade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='passaporte_numero',
            field=models.PositiveIntegerField(null=True, verbose_name=b'N\xc3\xbamero do Passaporte', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='passaporte_validade',
            field=models.DateField(null=True, verbose_name=b'Validade do Passaporte', blank=True),
        ),
    ]

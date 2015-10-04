# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0048_auto_20150929_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passaporte_emissao',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Pa\xc3\xads de Emiss\xc3\xa3o', blank=True),
        ),
    ]

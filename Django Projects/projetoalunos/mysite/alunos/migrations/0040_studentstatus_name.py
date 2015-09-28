# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0039_auto_20150928_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentstatus',
            name='name',
            field=models.CharField(default=b'Ativo', max_length=255, verbose_name=b'Status do Aluno'),
        ),
    ]

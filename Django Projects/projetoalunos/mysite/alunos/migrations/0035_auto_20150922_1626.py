# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0034_auto_20150922_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='orientador_aluno',
            field=models.ForeignKey(verbose_name=b'Orientador', to='alunos.Orientador'),
        ),
    ]

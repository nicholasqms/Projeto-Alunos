# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0028_auto_20150922_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='orientador_aluno',
            field=models.ForeignKey(default=b'1', to='alunos.Orientador'),
        ),
    ]

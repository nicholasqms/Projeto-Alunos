# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0029_student_orientador_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='orientador_aluno',
            field=models.ForeignKey(to='alunos.Orientador'),
        ),
    ]

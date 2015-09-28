# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0041_student_passaporte_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passaporte_validade',
            field=models.DateField(null=True, blank=True),
        ),
    ]

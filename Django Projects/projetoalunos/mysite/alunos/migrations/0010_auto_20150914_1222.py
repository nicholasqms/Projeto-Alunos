# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0009_studentuser_residence_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

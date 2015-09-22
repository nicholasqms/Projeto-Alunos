# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0024_auto_20150922_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orientador',
            old_name='birth_date',
            new_name='data_Nascimento',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='birth_date',
            new_name='data_Nascimento',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='birth_date',
            new_name='data_Nascimento',
        ),
        migrations.RenameField(
            model_name='teacheruser',
            old_name='birth_date',
            new_name='data_Nascimento',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0030_auto_20150922_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orientador',
            old_name='contact',
            new_name='contato',
        ),
        migrations.RenameField(
            model_name='orientador',
            old_name='register_number',
            new_name='numero_Registro',
        ),
    ]

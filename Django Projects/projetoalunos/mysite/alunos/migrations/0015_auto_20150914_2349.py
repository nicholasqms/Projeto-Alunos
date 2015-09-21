# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0014_auto_20150914_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacheruser',
            old_name='username',
            new_name='name',
        ),
    ]

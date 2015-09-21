# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0011_auto_20150914_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='teacheruser',
            old_name='name',
            new_name='username',
        ),
    ]

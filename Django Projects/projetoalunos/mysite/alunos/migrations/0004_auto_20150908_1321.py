# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_auto_20150908_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='grade_subject',
            new_name='subject',
        ),
    ]

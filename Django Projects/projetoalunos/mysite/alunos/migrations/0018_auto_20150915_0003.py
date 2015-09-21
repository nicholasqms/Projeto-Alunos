# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0017_auto_20150915_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='username',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'Username'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0038_auto_20150928_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.ForeignKey(verbose_name=b'Status do Aluno', to='alunos.StudentStatus'),
        ),
    ]

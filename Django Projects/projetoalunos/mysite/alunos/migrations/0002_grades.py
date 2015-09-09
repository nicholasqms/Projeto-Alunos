# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade_subject', models.CharField(max_length=100)),
                ('student_grade', models.DecimalField(max_digits=4, decimal_places=2)),
                ('student', models.ForeignKey(to='alunos.Student')),
            ],
        ),
    ]

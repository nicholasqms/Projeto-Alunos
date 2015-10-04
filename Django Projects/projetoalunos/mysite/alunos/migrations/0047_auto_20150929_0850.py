# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0046_auto_20150929_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='estado_expedicao',
            field=models.CharField(default=b'RJ', max_length=30, choices=[(b'Acre', b'AC'), (b'Alagoas', b'AL'), (b'Amap\xc3\xa1', b'AP'), (b'Amazonas', b'AM'), (b'Bahia', b'BA'), (b'Cear\xc3\xa1', b'CE'), (b'Distrito Federal', b'DF'), (b'Esp\xc3\xadrito Santo', b'ES'), (b'Goi\xc3\xa1s', b'GO'), (b'Maranh\xc3\xa3o', b'MA'), (b'Mato Grosso', b'MT'), (b'Mato Grosso do Sul', b'MS'), (b'Minas Gerais', b'MG'), (b'Par\xc3\xa1', b'PA'), (b'Para\xc3\xadba', b'PB'), (b'Paran\xc3\xa1', b'PR'), (b'Pernambuco', b'PE'), (b'Piau\xc3\xad', b'PI'), (b'Rio de Janeiro', b'RJ'), (b'Rio Grande do Norte', b'RN'), (b'Rio Grande do Sul', b'RS'), (b'Rond\xc3\xb4nia', b'RO'), (b'Roraima', b'RR'), (b'Santa Catarina', b'SC'), (b'S\xc3\xa3o Paulo', b'SP'), (b'Sergipe', b'SE'), (b'Tocantins', b'TO')]),
        ),
        migrations.AddField(
            model_name='student',
            name='orgao_expeditor',
            field=models.CharField(default=b'\xc3\x93rg\xc3\xa3o Expeditor', max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xx_Tab',
            fields=[
                ('pk_id', models.AutoField(serialize=False, primary_key=True)),
                ('xx_id', models.IntegerField()),
                ('xx_name', models.CharField(max_length=200)),
            ],
        ),
    ]

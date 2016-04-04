# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.IPAddressField()),
                ('osversion', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('disk', models.CharField(max_length=50)),
                ('vendor_id', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('cpu_core', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('Manufacturer', models.CharField(max_length=50)),
                ('sn', models.CharField(max_length=50)),
            ],
        ),
    ]

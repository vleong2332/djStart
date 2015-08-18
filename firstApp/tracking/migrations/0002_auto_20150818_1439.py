# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcharter',
            name='completion_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='op_responsible',
            field=models.CharField(help_text=b'Department or network that is responsible for this project', max_length=200, verbose_name=b'operational responsibility'),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='start_date',
            field=models.DateField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20150818_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcharter',
            name='content_aided',
            field=models.CharField(default='luke', help_text=b'What translated content is this project hoping to achieve?', max_length=50, choices=[(b'luke', b'Gospel of Luke'), (b'tA', b'Translation Audio'), (b'obs', b'OBS'), (b'ot', b'Other')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectcharter',
            name='content_other',
            field=models.CharField(help_text=b'Describe, if you chose "other" content.', max_length=50, null=True, verbose_name=b'Other content', blank=True),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='check_lvl',
            field=models.PositiveSmallIntegerField(help_text=b'', verbose_name=b'checking level', choices=[(1, b'1'), (2, b'2'), (3, b'3')]),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='funding_src',
            field=models.CharField(help_text=b'Who generally funds this project?', max_length=200, verbose_name=b'funding source'),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='output_other',
            field=models.CharField(help_text=b'Describe, if you chose "other" as medium.', max_length=50, null=True, verbose_name=b'other target', blank=True),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='output_target',
            field=models.CharField(help_text=b'Medium for the translation', max_length=2, choices=[(b'pr', b'Print'), (b'dg', b'Digital'), (b'au', b'Audio'), (b'ot', b'Other')]),
        ),
    ]

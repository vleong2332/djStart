# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('licensed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCharter',
            fields=[
                ('proj_name', models.CharField(unique=True, max_length=100, verbose_name=b'project name')),
                ('acc_num', models.CharField(max_length=10, serialize=False, verbose_name=b'account number', primary_key=True)),
                ('src_lang_name', models.CharField(help_text=b'The language of the source text', max_length=50, verbose_name=b'source language', choices=[(b'english', b'English'), (b'spanish', b'Spanish'), (b'german', b'German'), (b'france', b'France')])),
                ('src_lang_ietf', models.SlugField(max_length=20, verbose_name=b'source language IETF tag', choices=[(b'en', b'EN'), (b'sp', b'SP'), (b'de', b'DE'), (b'fr', b'FR')])),
                ('des_lang_name', models.CharField(help_text=b'The language of the translation', max_length=50, verbose_name=b'translation language', choices=[(b'english', b'English'), (b'spanish', b'Spanish'), (b'german', b'German'), (b'france', b'France')])),
                ('des_lang_ietf', models.SlugField(max_length=20, verbose_name=b'translation language IETF tag', choices=[(b'en', b'EN'), (b'sp', b'SP'), (b'de', b'DE'), (b'fr', b'FR')])),
                ('location_general', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date(2015, 8, 18))),
                ('completion_date', models.DateField(default=datetime.date(2025, 12, 31))),
                ('op_responsible', models.CharField(default=b'unknown', help_text=b'Department or network that is responsible for this project', max_length=200, verbose_name=b'operational responsibility')),
                ('funding_src', models.CharField(max_length=200)),
                ('output_target', models.CharField(max_length=2, choices=[(b'pr', b'Print'), (b'dg', b'Digital'), (b'au', b'Audio'), (b'ot', b'Other')])),
                ('output_other', models.CharField(max_length=50, null=True, blank=True)),
                ('check_lvl', models.PositiveSmallIntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3')])),
                ('check_workflow', models.TextField(max_length=1500)),
                ('content_flow', models.TextField(max_length=1500)),
                ('content_person', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='project',
            field=models.ForeignKey(to='tracking.ProjectCharter'),
        ),
    ]

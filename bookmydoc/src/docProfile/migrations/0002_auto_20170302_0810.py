# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('time_slot', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='bookdoc',
            name='end_time',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='bookdoc',
            name='start_time',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='locations',
            name='location',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]

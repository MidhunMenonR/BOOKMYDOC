# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('start_time', models.CharField(default=b'10:00 AM', max_length=8)),
                ('end_time', models.CharField(default=b'12:00 PM', max_length=8)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DocDetails',
            fields=[
                ('doc_username', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('doc_password', models.CharField(max_length=20)),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_location', models.CharField(max_length=50)),
                ('doc_phone', models.CharField(max_length=13)),
                ('doc_department', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=50)),
                ('doc_id', models.ForeignKey(to='docProfile.DocDetails')),
            ],
        ),
        migrations.AddField(
            model_name='bookdoc',
            name='loc_id',
            field=models.ForeignKey(to='docProfile.Locations'),
        ),
    ]

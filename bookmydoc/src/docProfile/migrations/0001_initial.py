# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('time_slot', models.CharField(max_length=5)),
                ('patientname', models.CharField(max_length=50)),
                ('patientphone', models.CharField(max_length=13)),
                ('date', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='BookDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=10)),
                ('start_time', models.CharField(max_length=5)),
                ('end_time', models.CharField(max_length=5)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DocDetails',
            fields=[
                ('doc_username', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('doc_password', models.CharField(max_length=20)),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_phone', models.CharField(max_length=13)),
                ('doc_department', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='EmergDoctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctor', models.CharField(unique=True, max_length=20)),
                ('regtoken', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(unique=True, max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=50)),
                ('doc_id', models.ForeignKey(to='docProfile.DocDetails')),
            ],
        ),
        migrations.AddField(
            model_name='bookdoc',
            name='loc_id',
            field=models.ForeignKey(to='docProfile.Locations'),
        ),
    ]

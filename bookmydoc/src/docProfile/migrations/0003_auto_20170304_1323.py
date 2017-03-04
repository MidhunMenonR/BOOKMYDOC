# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('docProfile', '0002_auto_20170302_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docdetails',
            name='doc_location',
        ),
        migrations.AddField(
            model_name='docdetails',
            name='email',
            field=models.EmailField(default=datetime.datetime(2017, 3, 4, 7, 52, 18, 661173, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docdetails',
            name='experience',
            field=models.CharField(default=datetime.datetime(2017, 3, 4, 7, 53, 7, 70498, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docdetails',
            name='image',
            field=models.ImageField(default=datetime.datetime(2017, 3, 4, 7, 53, 18, 753589, tzinfo=utc), upload_to=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docdetails',
            name='qualification',
            field=models.CharField(default=datetime.datetime(2017, 3, 4, 7, 53, 38, 447004, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locations',
            name='area',
            field=models.CharField(default=datetime.datetime(2017, 3, 4, 7, 53, 55, 959484, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]

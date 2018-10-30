# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20181030_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории', 'verbose_name': 'Категория'},
        ),
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterUniqueTogether(
            name='good',
            unique_together=set([('category', 'name', 'price', 'description')]),
        ),
    ]

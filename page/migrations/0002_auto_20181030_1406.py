# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': 'Товар', 'ordering': ['-price', 'name'], 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='good',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='good',
            unique_together=set([('category', 'name', 'price')]),
        ),
    ]

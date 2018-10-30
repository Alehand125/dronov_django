# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20181030_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ForeignKey(verbose_name='Категория', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.Category'),
        ),
        migrations.AlterField(
            model_name='good',
            name='description',
            field=models.TextField(verbose_name='Описание товара', default=' '),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.FloatField(verbose_name='Цена за единицу', default=0),
        ),
    ]

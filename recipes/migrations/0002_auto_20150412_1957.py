# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('unit_type', models.CharField(max_length=200)),
                ('unit_coeff', models.FloatField(default=1.0)),
            ],
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='amount_type',
            field=models.ForeignKey(to='recipes.Unit', default=None),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150412_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount_type',
            field=models.ForeignKey(to='recipes.Unit', default=None, blank=True, null=True),
        ),
    ]

# Generated by Django 5.2 on 2025-05-04 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget', to='api.category'),
        ),
    ]

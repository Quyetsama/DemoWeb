# Generated by Django 3.1.2 on 2020-10-25 14:34

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_post1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post1',
        ),
        migrations.AlterField(
            model_name='historymodel',
            name='title_history',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=255),
        ),
    ]
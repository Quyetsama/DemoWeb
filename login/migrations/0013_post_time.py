# Generated by Django 3.1.2 on 2020-10-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_historymodel_so_luong'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]

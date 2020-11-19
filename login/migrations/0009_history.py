# Generated by Django 3.1.2 on 2020-10-25 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('his_id', models.AutoField(primary_key=True, serialize=False)),
                ('clone_id', models.CharField(default='', max_length=9999)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

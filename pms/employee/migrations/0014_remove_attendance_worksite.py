# Generated by Django 3.1.3 on 2020-12-24 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_auto_20201216_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='worksite',
        ),
    ]
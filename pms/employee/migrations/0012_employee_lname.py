# Generated by Django 3.1.3 on 2020-12-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_category_num_of_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='lname',
            field=models.CharField(default='Sharma', max_length=30),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-04 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20201204_1828'),
        ('salary', '0003_remove_salary_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='salary',
            name='emp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AlterUniqueTogether(
            name='salary',
            unique_together={('emp', 'date')},
        ),
    ]

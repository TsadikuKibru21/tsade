# Generated by Django 4.1.4 on 2023-01-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDean', '0002_alter_dorm_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorm',
            name='Status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'InActive')], max_length=150),
        ),
    ]
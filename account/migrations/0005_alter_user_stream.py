# Generated by Django 4.1.6 on 2023-02-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_student_or_not'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stream',
            field=models.CharField(blank=True, choices=[('social', 'social'), ('natural', 'natural')], max_length=200, null=True),
        ),
    ]
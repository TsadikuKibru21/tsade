# Generated by Django 4.1.6 on 2023-02-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDean', '0004_placement_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='Status',
            field=models.CharField(choices=[('Active', 'Active'), ('InActive', 'InActive')], default=3, max_length=150),
            preserve_default=False,
        ),
    ]
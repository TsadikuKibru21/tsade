# Generated by Django 4.1.6 on 2023-02-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_departmnet_user_department_user_collage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Student_or_Not',
            field=models.CharField(choices=[('yes', 'Student'), ('no', 'Not Student')], default=2, max_length=50),
            preserve_default=False,
        ),
    ]
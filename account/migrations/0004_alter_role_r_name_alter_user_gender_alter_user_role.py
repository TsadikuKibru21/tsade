# Generated by Django 4.1.4 on 2022-12-10 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_departmnet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='R_name',
            field=models.CharField(default='Student', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='Role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.role'),
        ),
    ]
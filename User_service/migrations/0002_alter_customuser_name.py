# Generated by Django 4.2.3 on 2023-08-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank='', max_length=200),
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20220311_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date',
            field=models.DateField(max_length=20),
        ),
    ]

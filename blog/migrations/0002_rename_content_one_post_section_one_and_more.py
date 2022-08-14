# Generated by Django 4.0.4 on 2022-04-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_one',
            new_name='section_one',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content_two',
            new_name='section_two',
        ),
        migrations.AlterField(
            model_name='post',
            name='quote_author',
            field=models.CharField(default='Praise Media', max_length=50),
        ),
    ]

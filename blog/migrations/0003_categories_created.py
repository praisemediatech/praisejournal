# Generated by Django 4.0.4 on 2022-04-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_content_one_post_section_one_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
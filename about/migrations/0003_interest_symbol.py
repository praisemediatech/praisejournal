# Generated by Django 3.2.12 on 2022-03-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_interest_interest_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='symbol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
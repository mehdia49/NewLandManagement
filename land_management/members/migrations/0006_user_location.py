# Generated by Django 5.0 on 2023-12-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_landowner_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.TextField(default=' '),
        ),
    ]

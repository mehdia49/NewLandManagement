# Generated by Django 5.0 on 2023-12-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_infrastructure_infrastructure_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landowner',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]

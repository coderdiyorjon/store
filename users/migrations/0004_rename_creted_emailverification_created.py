# Generated by Django 3.2.12 on 2024-12-04 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20241204_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailverification',
            old_name='creted',
            new_name='created',
        ),
    ]

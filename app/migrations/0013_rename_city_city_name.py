# Generated by Django 4.2.2 on 2023-06-26 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_city_item_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='name',
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-26 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_pagesections_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagesections',
            name='name',
        ),
    ]

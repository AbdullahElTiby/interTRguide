# Generated by Django 4.2.2 on 2023-06-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_pagesections_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesections',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_sv_step10_alter_sv_step1_alter_sv_step2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='googlemapslink',
            field=models.TextField(blank=True, null=True),
        ),
    ]

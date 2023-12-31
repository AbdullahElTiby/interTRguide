# Generated by Django 4.2.2 on 2023-06-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_remove_item_audio_item_description13_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sv",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="photos")),
                ("title1", models.TextField(blank=True, null=True)),
                ("step1", models.CharField(max_length=255)),
                ("title2", models.TextField(blank=True, null=True)),
                ("step2", models.CharField(max_length=255)),
                ("title3", models.TextField(blank=True, null=True)),
                ("step3", models.CharField(max_length=255)),
                ("title4", models.TextField(blank=True, null=True)),
                ("step4", models.CharField(max_length=255)),
                ("title5", models.TextField(blank=True, null=True)),
                ("step5", models.CharField(max_length=255)),
                ("title6", models.TextField(blank=True, null=True)),
                ("step6", models.CharField(max_length=255)),
                ("title7", models.TextField(blank=True, null=True)),
                ("step7", models.CharField(max_length=255)),
                ("title8", models.TextField(blank=True, null=True)),
                ("step8", models.CharField(max_length=255)),
                ("title9", models.TextField(blank=True, null=True)),
                ("step9", models.CharField(max_length=255)),
                ("title10", models.TextField(blank=True, null=True)),
            ],
        ),
    ]

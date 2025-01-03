# Generated by Django 5.0.8 on 2024-12-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hidaya", "0003_remove_video_hls_playlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Partner",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Name"
                    ),
                ),
                (
                    "url",
                    models.CharField(db_index=True, max_length=255, verbose_name="URL"),
                ),
                ("logo", models.ImageField(upload_to="partners", verbose_name="Logo")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
            ],
            options={
                "verbose_name": "Partner",
                "verbose_name_plural": "Partners",
                "db_table": "partner",
                "ordering": ["-created_at"],
            },
        ),
    ]

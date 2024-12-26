# Generated by Django 5.0.8 on 2024-12-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hidaya", "0005_partner_name_en_partner_name_ru_partner_name_uz_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="type",
            field=models.CharField(
                choices=[("VIDEO", "Video"), ("YOUTUBE", "YouTube")],
                default="VIDEO",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="video",
            name="video_url",
            field=models.URLField(blank=True, null=True, verbose_name="Video URL"),
        ),
    ]
# Generated by Django 5.0.8 on 2024-12-19 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hidaya", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="hls_playlist",
        ),
    ]

# Generated by Django 5.0.8 on 2025-01-27 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hidaya", "0018_alter_latestnews_banner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="is_read",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="is_send",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="type",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="user",
        ),
    ]

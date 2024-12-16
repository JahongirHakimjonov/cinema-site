# Generated by Django 5.0.8 on 2024-12-16 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hidaya", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="type",
            field=models.CharField(
                choices=[("SINGLE", "Single"), ("ALL", "All")],
                default="SINGLE",
                max_length=10,
                verbose_name="Type",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]

# Generated by Django 5.0.8 on 2024-12-16 12:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hidaya", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
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
        migrations.AddField(
            model_name="order",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchases",
                to="hidaya.book",
                verbose_name="Book",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AddField(
            model_name="video",
            name="tags",
            field=models.ManyToManyField(
                related_name="videos", to="hidaya.tags", verbose_name="Tags"
            ),
        ),
        migrations.AddField(
            model_name="video",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="hidaya.videocategory",
                verbose_name="Category",
            ),
        ),
    ]

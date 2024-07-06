# Generated by Django 5.0.6 on 2024-07-06 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruitment", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="university",
            name="confirmed_students",
            field=models.ManyToManyField(
                blank=True,
                related_name="confirmed_universities",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
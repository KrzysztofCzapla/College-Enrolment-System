# Generated by Django 5.0.6 on 2024-07-06 18:02

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exam",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("MATH", "Math"),
                            ("ENGLISH", "English"),
                            ("FOREIGN_LANGUAGE", "Foreign Language"),
                            ("GEOGRAPHY", "Geography"),
                            ("BIOLOGY", "Biology"),
                            ("CHEMISTRY", "Chemistry"),
                            ("PHYSICS", "Physics"),
                            ("PHILOSOPHY", "Philosophy"),
                            ("COMPUTER_SCIENCE", "Computer Science"),
                            ("HISTORY", "History"),
                        ],
                        default="MATH",
                        max_length=255,
                    ),
                ),
                (
                    "score",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exams",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
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
                ("title", models.CharField(blank=True, max_length=255)),
                ("description", models.CharField(blank=True, max_length=5000)),
                ("max_number_of_students", models.IntegerField(default=100)),
                (
                    "exams_requirements",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.JSONField(), size=None
                    ),
                ),
                ("is_open", models.BooleanField(default=True)),
                (
                    "confirmed_students",
                    models.ManyToManyField(to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OfferStage",
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
                (
                    "number",
                    models.IntegerField(
                        default=1,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="offer_stages",
                        to="recruitment.offer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="University",
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
                ("address", models.CharField(blank=True, max_length=255)),
                (
                    "confirmed_students",
                    models.ManyToManyField(to=settings.AUTH_USER_MODEL),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="universities",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="offer",
            name="university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="offers",
                to="recruitment.university",
            ),
        ),
        migrations.CreateModel(
            name="Application",
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
                (
                    "priority",
                    models.IntegerField(
                        default=1,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("ACCEPTED", "Accepted"),
                            ("CONFIRMED", "Confirmed"),
                            ("REJECTED", "Rejected"),
                            ("RESIGNED", "Resigned"),
                        ],
                        default="PENDING",
                        max_length=255,
                    ),
                ),
                ("points", models.IntegerField(default=0)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="recruitment.offer",
                    ),
                ),
                (
                    "offer_stage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="recruitment.offerstage",
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="recruitment.university",
                    ),
                ),
            ],
        ),
    ]

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

from recruitment.models.university import University


class Offer(models.Model):
    title = models.CharField(max_length=255, blank=True)

    description = models.CharField(max_length=5000, blank=True)

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="offers")

    max_number_of_students = models.IntegerField(default=100)

    # where exam tier exists so there could be a choice at each exam tier
    # should be store as exams_requirements = [{"exams": [ExamTypes.MATH, ExamTypes.PHYSICS], "weight": "1.5"}]
    # each inside array is a tier
    exams_requirements = ArrayField(
        models.JSONField(),
    )

    confirmed_students = models.ManyToManyField(get_user_model())

    is_open = models.BooleanField(default=True)

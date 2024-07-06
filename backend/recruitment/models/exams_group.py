from django.contrib.auth import get_user_model
from django.db import models

from recruitment.models import Exam


class ExamsGroup(models.Model):
    owner = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="exams_group"
    )

    exams = models.ManyToManyField(Exam)

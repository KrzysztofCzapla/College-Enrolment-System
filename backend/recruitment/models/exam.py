from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from recruitment.enums import ExamTypes


class Exam(models.Model):
    name = models.CharField(
        max_length=255,
        choices=ExamTypes,
        default=ExamTypes.MATH
    )

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    score = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )

    def __str__(self):
        return self.name

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from recruitment.models import Exam, Offer, OfferStage, University


class Application(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="applications")

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="applications")

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="applications")

    offer_stage = models.ForeignKey(OfferStage, on_delete=models.CASCADE, related_name="applications")

    priority = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
    )

    exams = models.ManyToManyField(Exam)

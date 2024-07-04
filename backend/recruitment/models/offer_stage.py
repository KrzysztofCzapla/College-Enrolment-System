from django.core.validators import MinValueValidator
from django.db import models

from recruitment.models import Offer


class OfferStage(models.Model):
    # is it stage 1 or stage 2 etc
    number = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
    )

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    start_date = models.DateField()

    end_date = models.DateField()

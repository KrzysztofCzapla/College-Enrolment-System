from django.core.validators import MinValueValidator
from django.db import models

from django.contrib.auth import get_user_model


class OfferStage(models.Model):
    score = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ]
    )

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    address = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.name

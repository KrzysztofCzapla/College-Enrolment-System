from django.db import models

from django.contrib.auth import get_user_model


class University(models.Model):
    name = models.CharField(
        max_length=255
    )

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    address = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.name

from django.contrib.auth import get_user_model
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="universities")

    address = models.CharField(max_length=255, blank=True)

    confirmed_students = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.name

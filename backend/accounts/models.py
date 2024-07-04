from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.enums import AccountTypes


class CustomUser(AbstractUser):
    account_type = models.CharField(
        max_length=16,
        choices=AccountTypes,
        default=AccountTypes.STUDENT,
    )

    def __str__(self):
        return self.username
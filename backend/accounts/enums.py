from django.db import models


class AccountTypes(models.TextChoices):
    STUDENT = "STUDENT", "Student"
    UNIVERSITY_STAFF = "UNIVERSITY STAFF", "University Staff"
    ADMIN = "ADMIN", "Admin"

from django.db import models


class ExamTypes(models.TextChoices):
    MATH = "MATH", "Math"
    ENGLISH = "ENGLISH", "English"
    FOREIGN_LANGUAGE = "FOREIGN_LANGUAGE", "Foreign Language"
    GEOGRAPHY = "GEOGRAPHY", "Geography"
    BIOLOGY = "BIOLOGY", "Biology"
    CHEMISTRY = "CHEMISTRY", "Chemistry"
    PHYSICS = "PHYSICS", "Physics"
    PHILOSOPHY = "PHILOSOPHY", "Philosophy"
    COMPUTER_SCIENCE = "COMPUTER_SCIENCE", "Computer Science"
    HISTORY = "HISTORY", "History"


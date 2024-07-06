from django.contrib.auth import get_user_model

from recruitment.enums import ApplicationStatuses
from recruitment.models import Application


def change_application_status(application: Application, status: str):
    application.status = status
    application.save(update_fields=["status"])


def calculate_application_points(student: get_user_model(), application: Application):
    exams = student.exams_group.exams
    offer = application.offer

    application_points = 0

    for exams_tier in offer.exams_requirements:
        # Check if Student has at least one of the required exam for the tier
        if (
            highest_exam_score := exams.filter(name__in=exams_tier["exams"])
            .order_by("-score")
            .values_list("score", flat=True)
        ):
            application_points += highest_exam_score[0] * exams_tier["weight"]
        else:
            change_application_status(
                application=application, status=ApplicationStatuses.REJECTED
            )
            return

    application.points = application_points
    application.save(update_fields=["points"])

from celery import shared_task

from recruitment.enums import ApplicationStatuses
from recruitment.models import OfferStage
from recruitment.utils import change_application_status


@shared_task()
def calculate_stage_results(stage_id: int):
    offer_stage = OfferStage.objects.get(id=stage_id)
    applications = offer_stage.applications.filter(status=ApplicationStatuses.PENDING)
    offer = offer_stage.offer

    if not offer.is_open:
        applications.update(status=ApplicationStatuses.REJECTED)

    offer_max_number_of_students = offer.max_number_of_students
    offer_confirmed_students = offer.confirmed_students

    places_left_for_offer = offer_max_number_of_students - len(offer_confirmed_students)

    # Resign students that accepted other offers
    applications.filter(student__applications__status=ApplicationStatuses.CONFIRMED).update(status=ApplicationStatuses.RESIGNED)

    applications = applications.exclude(status=ApplicationStatuses.RESIGNED).order_by("-points")

    applications[:places_left_for_offer].update(status=ApplicationStatuses.ACCEPTED)
    applications[places_left_for_offer:].update(status=ApplicationStatuses.REJECTED)


@shared_task()
def confirm_stage(stage_id: int):
    offer_stage = OfferStage.objects.get(id=stage_id)
    offer_stage.applications.filter(status=ApplicationStatuses.ACCEPTED).update(status=ApplicationStatuses.RESIGNED)

    for application in offer_stage.applications.filter(status=ApplicationStatuses.CONFIRMED):
        application.university.confirmed_students.add(application.student)
        application.offer.confirmed_students.add(application.student)

        application.university.save(update_fields=["confirmed_students"])
        application.offer.save(update_fields=["confirmed_students"])



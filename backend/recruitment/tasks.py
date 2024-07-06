from celery import shared_task

from recruitment.enums import ApplicationStatuses
from recruitment.models import OfferStage


@shared_task()
def calculate_stage_results(stage_id: int):
    offer_stage = OfferStage.objects.get(id=stage_id)
    applications = offer_stage.applications.filter(status=ApplicationStatuses.PENDING)
    offer = offer_stage.offer

    if not offer.is_open:
        applications.update(status=ApplicationStatuses.REJECTED)

    offer_max_number_of_students = offer.max_number_of_students
    offer_confirmed_students = offer.confirmed_students

    places_left_for_offer = (
        offer_max_number_of_students - offer_confirmed_students.count()
    )

    # Resign students that accepted other offers
    applications.filter(
        student__applications__status=ApplicationStatuses.CONFIRMED
    ).update(status=ApplicationStatuses.RESIGNED)

    applications = applications.exclude(status=ApplicationStatuses.RESIGNED).order_by(
        "-points"
    )

    accepted_applications = applications.values("id")[:places_left_for_offer]
    rejected_applications = applications.values("id")[places_left_for_offer:]

    applications.filter(id__in=accepted_applications).update(
        status=ApplicationStatuses.ACCEPTED
    )
    applications.filter(id__in=rejected_applications).update(
        status=ApplicationStatuses.REJECTED
    )


@shared_task()
def confirm_stage(stage_id: int):
    offer_stage = OfferStage.objects.get(id=stage_id)
    offer_stage.applications.filter(status=ApplicationStatuses.ACCEPTED).update(
        status=ApplicationStatuses.RESIGNED
    )

    for application in offer_stage.applications.filter(
        status=ApplicationStatuses.CONFIRMED
    ):
        application.university.confirmed_students.add(application.student)
        application.offer.confirmed_students.add(application.student)

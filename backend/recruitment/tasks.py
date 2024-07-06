from celery import shared_task

from recruitment.enums import ApplicationStatuses
from recruitment.models import OfferStage
from recruitment.utils import change_application_status


@shared_task()
def calculate_stage_results(stage_id: int):
    """

    2.6)

    """
    # 1)
    offer_stage = OfferStage.objects.get(pk=stage_id)
    applications = offer_stage.applications.filter(status=ApplicationStatuses.PENDING)

    # 1.5)
    offer = offer_stage.offer

    if not offer.is_open:
        return

    offer_max_number_of_students = offer.max_number_of_students
    offer_confirmed_students = offer.confirmed_students

    places_left_for_offer = offer_max_number_of_students - len(offer_confirmed_students)

    # 2.1 REsign student sthat have accepted other offers
    applications.filter(student__applications__status=ApplicationStatuses.CONFIRMED).update(status=ApplicationStatuses.RESIGNED)

    applications = applications.exclude(status=ApplicationStatuses.RESIGNED).order_by("-points")

    applications[:places_left_for_offer].update(status=ApplicationStatuses.ACCEPTED)
    applications[places_left_for_offer:].update(status=ApplicationStatuses.REJECTED)



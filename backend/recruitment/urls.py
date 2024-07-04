from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.application import ApplicationViewSet
from .views.exam import ExamViewSet
from .views.offer import OfferViewSet
from .views.offer_stage import OfferStageViewSet
from .views.university import UniversityViewSet

router = DefaultRouter()
router.register(r"applications", ApplicationViewSet, basename="applications")
router.register(r"exams", ExamViewSet, basename="exams")
router.register(r"offers", OfferViewSet, basename="offers")
router.register(r"offer-stages", OfferStageViewSet, basename="offer-stages")
router.register(r"universities", UniversityViewSet, basename="universities")

urlpatterns = [
    path("", include(router.urls)),
]

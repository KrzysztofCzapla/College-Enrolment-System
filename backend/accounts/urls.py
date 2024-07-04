from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccountViewSet

router = DefaultRouter()
router.register(r"users", AccountViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]

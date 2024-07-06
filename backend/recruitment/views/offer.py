from rest_framework import permissions, viewsets

from accounts.enums import AccountTypes
from accounts.permissions import IsStaff
from recruitment.models import Offer
from recruitment.serializers.offer import OfferSerializer


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [
                IsStaff(),
            ]
        else:
            return [
                permissions.IsAuthenticated(),
            ]

    def get_queryset(self):
        if self.request.user.account_type != AccountTypes.ADMIN:
            return self.request.user.offers.all()
        else:
            return Offer.objects.all()

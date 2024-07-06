from rest_framework import permissions, viewsets

from accounts.permissions import IsStaff
from recruitment.models import University
from recruitment.serializers.university import UniversitySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer

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
        return University.objects.all()

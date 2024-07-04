from rest_framework import viewsets, permissions

from accounts.enums import AccountTypes
from accounts.permissions import IsStudent
from recruitment.models import Application
from recruitment.serializers.application import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsStudent(),]
        else:
            return [permissions.IsAuthenticated(),]

    def get_queryset(self):
        if self.request.user.account_type == AccountTypes.STUDENT:
            return self.request.user.applications.all()
        else:
            return Application.objects.all()

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from accounts.enums import AccountTypes
from accounts.permissions import IsStudent
from recruitment.models import Application
from recruitment.serializers.application import ApplicationSerializer
from recruitment.utils import calculate_application_points


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [
                IsStudent(),
            ]
        else:
            return [
                permissions.IsAuthenticated(),
            ]

    def get_queryset(self):
        if self.request.user.account_type == AccountTypes.STUDENT:
            return self.request.user.applications.all()
        else:
            return Application.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        calculate_application_points(
            student=serializer.instance.student, application=serializer.instance
        )

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

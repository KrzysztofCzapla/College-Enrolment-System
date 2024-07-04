from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = AccountSerializer

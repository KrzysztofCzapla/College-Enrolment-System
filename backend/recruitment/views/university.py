from rest_framework import viewsets, permissions

from recruitment.serializers.university import UniversitySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.universitys.all()

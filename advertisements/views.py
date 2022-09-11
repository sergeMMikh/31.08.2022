from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertisementFilter
    search_fields = ['creator', 'status', 'created_at', ]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "partial_update"]:
            self.permission_classes = [IsAuthenticated]
        if self.action in ["destroy", "update", ]:
            self.permission_classes = [IsOwnerOrReadOnly]

        return super(self.__class__, self).get_permissions()

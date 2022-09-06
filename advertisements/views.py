from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .serializers import AdvertisementSerializer


class DataFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        # fields = ['creator', 'status', 'created_at', ]
        exclude = []

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    filter_backends = [DjangoFilterBackend, ]
    # filterset_fields = ['creator', 'status', ]
    filterset_class = DataFilter
    search_fields = ['creator', 'status', 'created_at', ]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

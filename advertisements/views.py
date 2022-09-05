from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .serializers import AdvertisementSerializer


class DataFilter(FilterSet):
    date = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', ]


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ['creator', 'status', 'created_at']
    filterset_class = DataFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

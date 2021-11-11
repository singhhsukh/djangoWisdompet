from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from .models import Pet
from .serializers import PetSerializer


class PetsPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 20


class PetList(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('name','sex','species')
    search_fields = ('name','description')
    # pagination_class = PetsPagination

    def get_queryset(self):
        birthday = self.request.query_params.get("birthday",None)
        if birthday is None:
            return super().get_queryset()
        queryset = Pet.objects.all()
        if birthday.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                age__lte = 3
            )
        return queryset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    mixins,
    viewsets,
)

from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from tv_and_film_buffAPI.models import Series, Episodes
from tv_and_film_buffAPI.serializers import EpisodesSerializerList


class PaginationWithQueryParam(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100


class EpisodesViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pagination_class = PaginationWithQueryParam
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializerList
    lookup_url_kwarg = "imdbID"
    lookup_field = "imdbID"
    event = "RETRIEVE_EPISODE"
    filter_backends = (DjangoFilterBackend, SearchFilter)

    search_fields = ("imdbID",)

    def list(self, request, *args, **kwargs):
        """
        Return the list of all episodes
        """
        self.event = "LIST_EPISODES"
        return super().list(request, *args, **kwargs)

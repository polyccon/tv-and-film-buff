from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    mixins,
    viewsets,
)

from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from tv_and_film_buffAPI.filters import EpisodesListFilter
from tv_and_film_buffAPI.models import Series, Episodes, Comments
from tv_and_film_buffAPI.serializers import (
    CommentsSerializerList,
    EpisodesSerializerList,
    SeriesSerializerList,
)


class PaginationWithQueryParam(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100


class SeriesViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pagination_class = PaginationWithQueryParam
    queryset = Series.objects.all()
    serializer_class = SeriesSerializerList
    event = "RETRIEVE_SERIES"
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("series_id",)

    def list(self, request, *args, **kwargs):
        """
        Return the list of all series
        """
        self.event = "LIST_SERIES"
        return super().list(request, *args, **kwargs)


class EpisodesViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pagination_class = PaginationWithQueryParam
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializerList
    lookup_url_kwarg = "imdb_id"
    lookup_field = "imdb_id"
    event = "RETRIEVE_EPISODE"
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("imdb_id",)

    def list(self, request, *args, **kwargs):
        """
        Return the list of all episodes
        """
        self.event = "LIST_EPISODES"
        self.filterset_class = EpisodesListFilter
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific episode.
        """
        self.event = "RETRIEVE_EPISODE"

        return super().retrieve(request, *args, **kwargs)


class CommentsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializerList
    lookup_field = "id"

    def list(self, request, *args, **kwargs):
        """
        Return the list of all comments
        """
        self.event = "LIST_COMMENTS"
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create a comment for an episode
        """
        self.event = "CREATE_COMMENTS"
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update a comment for an episode
        """
        self.event = "UPDATE_COMMENT"
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a comment for an episode
        """
        self.event = "DELETE_COMMENT"
        return super().destroy(request, *args, **kwargs)

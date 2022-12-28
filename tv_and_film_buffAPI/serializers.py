from rest_framework import serializers

from tv_and_film_buffAPI.models import Series, Episodes, Comments


class EpisodesSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = (
            "imdb_id",
            "title",
            "plot",
            "season_number",
            "episode_number",
            "genre",
            "language",
            "imdb_rating",
            "poster",
            "series",
            "comments",
        )


class CommentsSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            "body",
            "episode",
        )


class SeriesSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = "__all__"
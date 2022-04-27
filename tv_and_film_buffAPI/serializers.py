from rest_framework import serializers

from tv_and_film_buffAPI.models import Series, Episodes


class EpisodesSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = (
            "imdbID",
            "title",
            "plot",
            "season_number",
            "episode_number",
            "genre",
            "language",
            "imdbRating",
            "poster",
            "series",
        )

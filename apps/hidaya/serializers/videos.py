from rest_framework import serializers

from apps.hidaya.models import Video
from apps.hidaya.serializers import TagsSerializer, VideoCategorySerializer


class VideoSerializer(serializers.ModelSerializer):
    tags = TagsSerializer()
    category = VideoCategorySerializer()

    class Meta:
        model = Video
        fields = (
            "id",
            "title",
            "description",
            "banner",
            "tags",
            "category",
            "date",
            "hls_playlist",
        )

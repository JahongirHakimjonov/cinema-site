from rest_framework import serializers

from apps.hidaya.models import News
from apps.hidaya.serializers import NewsCategorySerializer


class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "sub_title",
            "description",
            "banner",
            "category",
            "view_count",
            "created_at",
        )

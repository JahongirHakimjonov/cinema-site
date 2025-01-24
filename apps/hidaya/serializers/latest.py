from rest_framework import serializers

from apps.hidaya.models import LatestNews


class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNews
        fields = "__all__"

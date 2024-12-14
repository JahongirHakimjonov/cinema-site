from rest_framework import serializers

from apps.hidaya.models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ("id", "title", "description", "created_at")

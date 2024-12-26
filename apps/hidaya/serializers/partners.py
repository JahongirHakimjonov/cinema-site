from rest_framework import serializers

from apps.hidaya.models import Partner, Platform


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ("id", "name", "logo", "url", "created_at")


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ("id", "logo", "text", "image", "title", "description", "created_at")

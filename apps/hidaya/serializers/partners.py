from rest_framework import serializers

from apps.hidaya.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ("id", "name", "logo", "url", "created_at")

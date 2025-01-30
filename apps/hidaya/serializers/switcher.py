from rest_framework import serializers

from apps.hidaya.models.switcher import Switcher


class SwitcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switcher
        fields = "__all__"
        read_only_fields = ("id",)

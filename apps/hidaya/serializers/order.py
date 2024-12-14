from rest_framework import serializers

from apps.hidaya.models import Order
from apps.hidaya.serializers import BookSerializer
from apps.users.serializers import MeSerializer


class OrderSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = MeSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "book",
            "format",
            "address",
            "payment_status",
            "total_price",
            "payment_method",
            "created_at",
            "updated_at",
        )
        read_only_fields = ["id", "created_at", "updated_at"]

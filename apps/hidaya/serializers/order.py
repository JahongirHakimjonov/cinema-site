from rest_framework import serializers

from apps.hidaya.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
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
        extra_kwargs = {
            "payment_status": {"read_only": True},
            "total_price": {"read_only": True},
            "payment_method": {"read_only": True},
        }

    def create(self, validated_data):
        user = self.context["request"].user
        order = Order.objects.create(user=user, **validated_data)
        return order

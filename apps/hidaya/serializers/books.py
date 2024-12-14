from rest_framework import serializers

from apps.hidaya.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ("id", "title", "author", "banner", "category")

    def get_category(self, obj):
        from apps.hidaya.serializers import BookCategorySerializer

        return BookCategorySerializer(obj.category).data


class BookDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "sub_title",
            "description",
            "author",
            "banner",
            "pages",
            "date",
            "price",
            "discount_price",
            "category",
            "genre",
            "is_active",
            "file",
            "sold_count",
            "created_at",
        )

    def get_category(self, obj):
        from apps.hidaya.serializers import BookCategorySerializer
        return BookCategorySerializer(obj.category).data

    def get_genre(self, obj):
        from apps.hidaya.serializers import GenreSerializer
        return GenreSerializer(obj.genre, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context['request'].user
        order = Order.objects.filter(user=user, book=instance, payment_status=True).exists()
        representation['is_purchased'] = order
        if order:
            representation['original_file'] = instance.original_file.url

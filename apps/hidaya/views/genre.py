from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import BookCategory, NewsCategory, VideoCategory
from apps.hidaya.serializers import (
    BookCategorySerializer,
    NewsCategorySerializer,
    VideoCategorySerializer,
)


class BookCategoryList(APIView):
    serializer_class = BookCategorySerializer
    permission_classes = [AllowAny]

    def get(self, request):
        book_categories = BookCategory.objects.filter(is_active=True)
        serializer = self.serializer_class(book_categories, many=True)
        return Response(
            {
                "success": True,
                "message": "Book categories fetched successfully.",
                "data": serializer.data,
            }
        )


class NewsCategoryList(APIView):
    serializer_class = NewsCategorySerializer
    permission_classes = [AllowAny]

    def get(self, request):
        news_categories = NewsCategory.objects.filter(is_active=True)
        serializer = self.serializer_class(news_categories, many=True)
        return Response(
            {
                "success": True,
                "message": "News categories fetched successfully.",
                "data": serializer.data,
            }
        )


class VideoCategoryList(APIView):
    serializer_class = VideoCategorySerializer
    permission_classes = [AllowAny]

    def get(self, request):
        video_categories = VideoCategory.objects.filter(is_active=True)
        serializer = self.serializer_class(video_categories, many=True)
        return Response(
            {
                "success": True,
                "message": "Video categories fetched successfully.",
                "data": serializer.data,
            }
        )

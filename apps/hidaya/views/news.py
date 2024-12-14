from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import News
from apps.hidaya.serializers import NewsSerializer
from apps.shared.pagination import CustomPagination


class NewsList(APIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get(self, request):
        news = News.objects.filter(is_active=True)
        paginator = self.pagination_class()
        paginated_news = paginator.paginate_queryset(news, request)
        serializer = self.serializer_class(paginated_news, many=True)
        return paginator.get_paginated_response(serializer.data)


class NewsDetail(APIView):
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        news = News.objects.get(pk=pk, is_active=True)
        news.increment_views()
        serializer = self.serializer_class(news)
        return Response(serializer.data)

from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
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

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="search",
                description="Search term for filtering news by title or description",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="category",
                description="Category for filtering news",
                required=False,
                type=str,
            ),
        ],
        responses=NewsSerializer(many=True),
    )
    def get(self, request):
        search = request.query_params.get("search")
        category = request.query_params.get("category")
        news = News.objects.filter(is_active=True)

        if category:
            news = news.filter(category=category)

        if search:
            search_terms = search[:100].split()
            query = Q()
            for term in search_terms:
                query &= (
                    Q(title__icontains=term)
                    |Q(title_uz__icontains=term)
                    |Q(title_ru__icontains=term)
                    |Q(title_en__icontains=term)
                    |Q(title_ko__icontains=term)
                    | Q(sub_title__icontains=term)
                    | Q(sub_title_uz__icontains=term)
                    | Q(sub_title_ru__icontains=term)
                    | Q(sub_title_en__icontains=term)
                    | Q(sub_title_ko__icontains=term)
                    | Q(description__icontains=term)
                    | Q(description_uz__icontains=term)
                    | Q(description_ru__icontains=term)
                    | Q(description_en__icontains=term)
                    | Q(description_ko__icontains=term)
                )
            news = news.filter(query).distinct()

        paginator = self.pagination_class()
        paginated_news = paginator.paginate_queryset(news, request)
        serializer = self.serializer_class(paginated_news, many=True)
        return paginator.get_paginated_response(serializer.data)


class NewsDetail(APIView):
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        news = News.objects.filter(pk=pk, is_active=True).last()
        if not news:
            return Response(
                {"success": False, "message": "News not found."}, status=404
            )
        news.increment_views()
        serializer = self.serializer_class(news)
        return Response(
            {
                "success": True,
                "message": "News fetched successfully.",
                "data": serializer.data,
            }
        )

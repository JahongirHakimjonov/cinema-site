from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Video
from apps.hidaya.serializers import VideoSerializer
from apps.shared.pagination import CustomPagination


class VideoList(APIView):
    serializer_class = VideoSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="search",
                description="Search term for filtering videos by title or description",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="category",
                description="Category for filtering videos",
                required=False,
                type=str,
            ),
        ],
        responses=VideoSerializer(many=True),
    )
    def get(self, request):
        search = request.query_params.get("search")
        category = request.query_params.get("category")
        videos = Video.objects.filter(is_active=True)

        if search:
            search_terms = search[:100].split()
            query = Q()
            for term in search_terms:
                query &= (
                    Q(title__icontains=term)
                    | Q(title_uz__icontains=term)
                    | Q(title_tr__icontains=term)
                    | Q(title_en__icontains=term)
                    | Q(title_ko__icontains=term)
                    | Q(description__icontains=term)
                    | Q(description_uz__icontains=term)
                    | Q(description_tr__icontains=term)
                    | Q(description_en__icontains=term)
                    | Q(description_ko__icontains=term)
                )
            videos = videos.filter(query).distinct()

        if category:
            videos = videos.filter(category=category)

        paginator = self.pagination_class()
        paginated_videos = paginator.paginate_queryset(videos, request)
        serializer = self.serializer_class(paginated_videos, many=True)
        return paginator.get_paginated_response(serializer.data)


class VideoDetail(APIView):
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        video = Video.objects.filter(pk=pk, is_active=True).last()
        if not video:
            return Response(
                {"success": False, "message": "Video not found."}, status=404
            )
        video.increment_views()
        serializer = self.serializer_class(video)
        return Response(
            {
                "success": True,
                "message": "Video fetched successfully.",
                "data": serializer.data,
            }
        )

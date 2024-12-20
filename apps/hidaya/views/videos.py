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

    def get(self, request):
        videos = Video.objects.filter(is_active=True)
        paginator = self.pagination_class()
        paginated_videos = paginator.paginate_queryset(videos, request)
        serializer = self.serializer_class(paginated_videos, many=True)
        return paginator.get_paginated_response(serializer.data)


class VideoDetail(APIView):
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        video = Video.objects.get(pk=pk, is_active=True)
        video.increment_views()
        serializer = self.serializer_class(video)
        return Response(
            {
                "success": True,
                "message": "Video fetched successfully.",
                "data": serializer.data,
            }
        )

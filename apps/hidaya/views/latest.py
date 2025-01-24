from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import LatestNews
from apps.hidaya.serializers import LatestNewsSerializer


class LatestNewsView(APIView):
    serializer_class = LatestNewsSerializer

    def get_queryset(self):
        return LatestNews.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        latest_news = self.get_queryset()
        serializer = self.serializer_class(latest_news, many=True)
        return Response(
            {
                "success": True,
                "message": "Latest news fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

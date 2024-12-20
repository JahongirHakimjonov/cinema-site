from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Info
from apps.hidaya.serializers import InfoSerializer
from apps.shared.pagination import CustomPagination


class InfoList(APIView):
    serializer_class = InfoSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get(self, request):
        info = Info.objects.filter(is_active=True)
        paginator = self.pagination_class()
        paginated_info = paginator.paginate_queryset(info, request)
        serializer = self.serializer_class(paginated_info, many=True)
        return paginator.get_paginated_response(serializer.data)


class InfoDetail(APIView):
    serializer_class = InfoSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        info = Info.objects.get(pk=pk, is_active=True)
        serializer = self.serializer_class(info)
        return Response(
            {
                "success": True,
                "message": "Info fetched successfully.",
                "data": serializer.data,
            }
        )

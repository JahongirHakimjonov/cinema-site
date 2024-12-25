from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
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

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="search",
                description="Search term for filtering info by title or description",
                required=False,
                type=str,
            )
        ],
        responses=InfoSerializer(many=True),
    )
    def get(self, request):
        search = request.query_params.get("search")
        info = Info.objects.filter(is_active=True)

        if search:
            search_terms = search[:100].split()
            query = Q()
            for term in search_terms:
                query &= Q(title__icontains=term) | Q(description__icontains=term)
            info = info.filter(query).distinct()

        paginator = self.pagination_class()
        paginated_info = paginator.paginate_queryset(info, request)
        serializer = self.serializer_class(paginated_info, many=True)
        return paginator.get_paginated_response(serializer.data)


class InfoDetail(APIView):
    serializer_class = InfoSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        info = Info.objects.filter(pk=pk, is_active=True).last()
        if not info:
            return Response(
                {"success": False, "message": "Info not found."}, status=404
            )
        serializer = self.serializer_class(info)
        return Response(
            {
                "success": True,
                "message": "Info fetched successfully.",
                "data": serializer.data,
            }
        )

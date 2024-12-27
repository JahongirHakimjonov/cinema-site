from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Partner, Platform, Author
from apps.hidaya.serializers import (
    PartnerSerializer,
    PlatformSerializer,
    AuthorSerializer,
)


class PartnerList(APIView):
    serializer_class = PartnerSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        partners = Partner.objects.filter(is_active=True)
        serializer = self.serializer_class(partners, many=True)
        return Response(
            {
                "success": True,
                "message": "Partners fetched successfully.",
                "data": serializer.data,
            }
        )


class PlatformList(APIView):
    serializer_class = PlatformSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        platforms = Platform.objects.all()
        serializer = self.serializer_class(platforms, many=True)
        return Response(
            {
                "success": True,
                "message": "Platforms fetched successfully.",
                "data": serializer.data,
            }
        )


class AuthorList(APIView):
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        authors = Author.objects.all()
        serializer = self.serializer_class(authors, many=True)
        return Response(
            {
                "success": True,
                "message": "Authors fetched successfully.",
                "data": serializer.data,
            }
        )

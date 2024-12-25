from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Partner
from apps.hidaya.serializers import PartnerSerializer


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

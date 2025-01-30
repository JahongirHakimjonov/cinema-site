from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Switcher
from apps.hidaya.serializers import SwitcherSerializer


class SwitcherAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SwitcherSerializer

    def get(self, request):
        switcher = Switcher.objects.first()
        serializer = self.serializer_class(switcher)
        return Response(
            {
                "success": True,
                "message": "Switcher fetched successfully.",
                "data": serializer.data,
            }
        )

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Notification
from apps.hidaya.serializers import NotificationSerializer


class NotificationView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)
        serializer = self.serializer_class(notifications, many=True)
        return Response(
            {
                "success": True,
                "message": "Notifications fetched successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        notification_id = request.data.get("notification_id")
        notification = Notification.objects.get(id=notification_id)
        notification.is_read = True
        notification.save()
        return Response(
            {
                "success": True,
                "message": "Notification read successfully.",
                "data": self.serializer_class(notification).data,
            },
            status=status.HTTP_200_OK,
        )

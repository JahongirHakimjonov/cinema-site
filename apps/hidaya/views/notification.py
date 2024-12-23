from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Notification
from apps.hidaya.serializers import NotificationSerializer
from apps.shared.pagination import CustomPagination


class NotificationView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    pagination_class = CustomPagination

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="is_read",
                description="Filter notifications by read status",
                required=False,
                type=bool,
            )
        ],
        responses=NotificationSerializer(many=True),
    )
    def get(self, request):
        is_read = request.query_params.get("is_read")
        notifications = Notification.objects.filter(user=request.user)

        if is_read is not None:
            notifications = notifications.filter(is_read=is_read)

        paginator = self.pagination_class()
        paginated_notifications = paginator.paginate_queryset(notifications, request)
        serializer = self.serializer_class(paginated_notifications, many=True)

        return paginator.get_paginated_response(serializer.data)

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "notification_id": {
                        "type": "integer",
                        "description": "ID of the notification to mark as read"
                    }
                },
                "required": ["notification_id"]
            }
        },
        responses={
            200: NotificationSerializer,
            404: OpenApiExample(
                "Notification not found",
                value={"success": False, "message": "Notification not found."}
            )
        }
    )
    def post(self, request):
        notification_id = request.data.get("notification_id")
        notification = Notification.objects.get(id=notification_id, user=request.user)
        if not notification:
            return Response(
                {"success": False, "message": "Notification not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
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

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.hidaya.models import Notification
from apps.hidaya.serializers import NotificationSerializer
from apps.shared.pagination import CustomPagination


class NotificationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = NotificationSerializer
    pagination_class = CustomPagination

    def get(self, request):
        notifications = Notification.objects.all()
        paginator = self.pagination_class()
        paginated_notifications = paginator.paginate_queryset(notifications, request)
        serializer = self.serializer_class(paginated_notifications, many=True)
        return paginator.get_paginated_response(serializer.data)

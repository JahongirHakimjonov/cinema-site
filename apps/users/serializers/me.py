from rest_framework import serializers

from apps.users.models import User, ActiveSessions


class MeSerializer(serializers.ModelSerializer):
    session_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "first_name",
            "last_name",
            "avatar",
            "session_id",
            "created_at",
            "updated_at",
        ]

    def get_session_id(self, obj):
        request = self.context.get("request")
        access_token = (
            request.headers.get("Authorization").split(" ")[1]
            if request and "Authorization" in request.headers
            else None
        )
        session = ActiveSessions.objects.filter(
            user=obj, is_active=True, access_token=access_token
        ).first()
        return session.id if session else None

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.hidaya.models import Notification, NotificationType
from apps.users.models import ActiveSessions
from apps.users.serializers import (
    CustomTokenObtainPairSerializer,
    BlockSessionSerializer,
    ActiveSessionsSerializer,
)
from apps.users.serializers import CustomTokenRefreshSerializer
from apps.users.services import RegisterService


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        jwt_token = serializer.validated_data

        ip_address = RegisterService.get_client_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown User Agent")
        location = RegisterService.get_location(ip_address)
        refresh_token = jwt_token.get("refresh")
        access_token = jwt_token.get("access")
        user_id = jwt_token.get("user")

        active_session = ActiveSessions.objects.create(
            user_id=user_id,
            ip=ip_address,
            user_agent=user_agent,
            location=location,
            refresh_token=refresh_token,
            access_token=access_token,
        )
        address = f"{active_session.location.get('country', '')}, {active_session.location.get('city', '')}"
        latitude = active_session.location.get('lat', '')
        longitude = active_session.location.get('lon', '')
        coordinates = f"{latitude}, {longitude}"
        ip = active_session.ip
        device = active_session.user_agent
        isp = active_session.location.get('isp', '')
        timezone = active_session.location.get('timezone', '')
        created_at = active_session.created_at.strftime("%Y-%m-%d  %H:%M:%S")

        messages = {
            "uz": f"Akkauntizga soat {created_at} da {address} dan kirildi, Kordinatalar: {coordinates}, IP: {ip}, Qurilma: {device}, ISP: {isp}, Timezone: {timezone}",
            "ru": f"Ваш аккаунт был вошел в {created_at} из {address}, Координаты: {coordinates}, IP: {ip}, Устройство: {device}, ISP: {isp}, Timezone: {timezone}",
            "en": f"Your account was logged in at {created_at} from {address}, Coordinates: {coordinates}, IP: {ip}, Device: {device}, ISP: {isp}, Timezone: {timezone}",
            "uz_Cyrl": f"Аккаунтингизга соат {created_at} да {address} дан кирилди, Кординаталар: {coordinates}, IP: {ip}, Қурилма: {device}, ISP: {isp}, Timezone: {timezone}",
        }

        Notification.objects.create(
            user_id=user_id,
            title_uz="Yangi kirish",
            title_ru="Новый вход",
            title_en="New login",
            title_uz_Cyrl="Янги кириш",
            message_uz=messages["uz"],
            message_ru=messages["ru"],
            message_en=messages["en"],
            message_uz_Cyrl=messages["uz_Cyrl"],
            type=NotificationType.SINGLE,
        )

        return Response({"refresh": refresh_token, "access": access_token})


class CustomTokenRefreshView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data["refresh"]

        try:
            token = RefreshToken(refresh_token)
            user_id = token["user_id"]

            session = ActiveSessions.objects.filter(
                user_id=user_id, refresh_token=refresh_token, is_active=True
            ).first()
            if not session:
                return Response(
                    {"error": "Invalid refresh token"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            new_access_token = str(token.access_token)
            # new_refresh_token = str(token)

            session.access_token = new_access_token
            # session.refresh_token = new_refresh_token
            session.save()

            return Response({"access": new_access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BlockSessionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlockSessionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        session_id = serializer.validated_data["session_id"]

        try:
            session = ActiveSessions.objects.get(id=session_id, user=request.user)
            session.is_active = False
            session.access_token = ""
            session.refresh_token = ""
            session.save()

            return Response(
                {"message": "Session blocked successfully"}, status=status.HTTP_200_OK
            )
        except ActiveSessions.DoesNotExist:
            return Response(
                {"error": "Session not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ListSessionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActiveSessionsSerializer

    def get(self, request, *args, **kwargs):
        sessions = ActiveSessions.objects.filter(user=request.user, is_active=True)
        serializer = self.serializer_class(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

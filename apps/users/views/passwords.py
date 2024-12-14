import uuid

from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework import status, response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.shared.exceptions import SmsException
from apps.users.models import ResetToken, User
from apps.users.serializers import (
    ChangePasswordSerializer,
    SendPasswordResetSerializer,
    ResetConfirmationSerializer,
    PasswordResetSerializer,
)
from apps.users.services import UserService, SmsService


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"detail": "Password changed successfully."})


class SendPasswordResetView(GenericAPIView, UserService):
    serializer_class = SendPasswordResetSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone"]
        self.send_confirmation(self, phone)
        return JsonResponse({"detail": "Password reset code sent."})


class ResetConfirmationCodeView(APIView, UserService):
    """Reset confirm otp code"""

    serializer_class = ResetConfirmationSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)

        data = ser.data
        code, phone = data.get("code"), data.get("phone")
        try:
            res = SmsService.check_confirm(phone, code)
            if res:
                token = ResetToken.objects.create(
                    user=User.objects.filter(phone=phone).first(),
                    token=str(uuid.uuid4()),
                )
                return response.Response(
                    data={
                        "token": token.token,
                        "created_at": token.created_at,
                        "updated_at": token.updated_at,
                    },
                    status=status.HTTP_200_OK,
                )
            return response.Response(
                data={"detail": _("Tasdiqlash ko'di xato")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except SmsException as e:
            return response.Response(
                {"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return response.Response({"detail": e}, status=status.HTTP_400_BAD_REQUEST)


class ResetSetPasswordView(APIView, UserService):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        token = data.get("token")
        password = data.get("new_password")
        token = ResetToken.objects.filter(token=token)
        if not token.exists():
            return response.Response(
                {"detail": _("Token xato")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        phone = token.first().user.phone
        token.delete()
        self.change_password(self, phone, password)
        return response.Response(
            {"detail": _("Parol yangilandi")}, status=status.HTTP_200_OK
        )

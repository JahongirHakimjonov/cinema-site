import os

import redis
from django.db import IntegrityError
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from apps.shared.exceptions import SmsException
from apps.users.models import User
from apps.users.serializers import (
    RegisterSerializer,
    ConfirmSerializer,
    ResendSerializer,
)
from apps.users.services import SmsService
from apps.users.services.users import UserService

redis_instance = redis.StrictRedis.from_url(os.getenv("REDIS_CACHE_URL"))


class RegisterView(APIView, UserService):
    permission_classes = [AllowAny]
    throttle_classes = [UserRateThrottle]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            redis_instance.hmset(phone, serializer.validated_data)
            self.send_confirmation(self, phone)
            return Response(
                {
                    "success": True,
                    "message": _("Registration data saved. Please confirm your code."),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "message": _("Invalid data."),
                "data": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class ConfirmView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            code = serializer.validated_data["code"]
            user = None
            try:
                if SmsService.check_confirm(phone, code=code):
                    user_data = redis_instance.hgetall(phone)
                    if user_data:
                        try:
                            user = User.objects.create_user(
                                phone=phone,
                                first_name=user_data[b"first_name"].decode("utf-8"),
                                last_name=user_data[b"last_name"].decode("utf-8"),
                                password=user_data[b"password"].decode("utf-8"),
                            )
                            redis_instance.delete(phone)
                        except IntegrityError as e:
                            if "duplicate key value violates unique constraint" in str(
                                e
                            ):
                                return Response(
                                    {
                                        "success": False,
                                        "message": _("Phone number already exists."),
                                    },
                                    status=status.HTTP_400_BAD_REQUEST,
                                )
                            return Response(
                                {"success": False, "message": str(e)},
                                status=status.HTTP_400_BAD_REQUEST,
                            )
                    token = user.tokens()
                    return Response(token, status=status.HTTP_201_CREATED)
            except SmsException as e:
                return Response(
                    {"success": False, "message": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Exception as e:
                return Response(
                    {"success": False, "message": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                {"success": False, "message": _("Invalid phone number or code.")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "success": False,
                "message": _("Invalid data."),
                "data": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class ResendView(APIView, UserService):
    serializer_class = ResendSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get("phone")
        self.send_confirmation(self, phone)
        return Response(
            {
                "success": True,
                "message": _(f"Confirmation code sent to {phone} phone number."),
            },
            status=status.HTTP_200_OK,
        )

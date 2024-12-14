from django.http import JsonResponse
from django.utils.translation import gettext as _
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import response, status
from rest_framework.views import APIView

from apps.users.serializers import UpdateAvatarSerializer, UpdateUserSerializer
from ..serializers import DeleteAccountSerializer


class UpdateAvatarView(APIView):
    serializer_class = UpdateAvatarSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.update(request.user, serializer.validated_data)
        return JsonResponse(self.serializer_class(updated_instance).data)


class UpdateUserView(APIView):
    serializer_class = UpdateUserSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.update(request.user, serializer.validated_data)
        return JsonResponse(self.serializer_class(updated_instance).data)


class DeleteAccountView(APIView):
    """usaer delete view"""

    serializer_class = DeleteAccountSerializer

    @extend_schema(
        request=serializer_class,
        responses={200: OpenApiResponse(DeleteAccountSerializer)},
        summary=_("Foydalanuvchi hisobini o'chirish."),
        description=_("Autentifikatsiya qilingan foydalanuvchi hisobini o'chirish."),
    )
    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        if user.check_password(request.data["password"]):
            user.delete()
            return response.Response(
                data={"detail": _("Hisob muvaffaqiyatli o'chirildi")},
                status=status.HTTP_200_OK,
            )
        return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"detail": _("Parol noto'g'ri kiritildi.")},
        )

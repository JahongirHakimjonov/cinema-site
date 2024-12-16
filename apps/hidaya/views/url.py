import hashlib

from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.hidaya.utils import generate_signed_url
from core import settings

my_key = settings.SECRET_KEY


class GetSignedVideoURLView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, video_id, quality, file_name):
        key = request.data.get("key")
        if not key:
            return JsonResponse({"error": "Key is required"}, status=400)
        combined_key = f"{my_key}{video_id}{quality}{file_name}"
        hashed_key = hashlib.sha256(combined_key.encode()).hexdigest()
        if key != hashed_key:
            return JsonResponse({"error": "Invalid key"}, status=400)
        path = f"/media/hls_videos/{video_id}/{quality}/{file_name}"
        signed_url = generate_signed_url(path, expiration=300)
        return JsonResponse({"signed_url": signed_url})

import hashlib

from django.conf import settings
from django.core.cache import cache
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.utils import generate_signed_url


class GetSignedVideoURLView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, video_id, quality, file_name):
        key = request.data.get("key")
        client_ip = request.META.get('REMOTE_ADDR')

        if not key:
            return Response({"error": "Key is required"}, status=400)

        if not client_ip:
            return Response({"error": "Could not determine client IP"}, status=400)

        cache_key = f"rate_limit_{client_ip}"
        request_count = cache.get(cache_key, 0)
        request_rate_limit = getattr(settings, 'RATE_LIMIT', 10)
        if request_count >= int(request_rate_limit):
            return Response({"error": "Rate limit exceeded"}, status=429)
        cache.set(cache_key, request_count + 1, timeout=60)

        combined_key = f"{video_id}{quality}{file_name}"
        hashed_key = hashlib.sha256(combined_key.encode()).hexdigest()

        if key != hashed_key:
            return Response({"error": "Invalid key"}, status=400)

        path = f"/media/hls_videos/{video_id}/{quality}/{file_name}"

        expiration_time = getattr(settings, 'SIGNED_URL_EXPIRATION', 60)
        signed_url = generate_signed_url(path, expiration=int(expiration_time))

        # if not request.is_secure():
        #     return Response({"error": "Request must be over HTTPS"}, status=400)

        return Response(
            {
                "success": True,
                "message": "Signed URL generated successfully.",
                "data": {"signed_url": signed_url},
            }
        )

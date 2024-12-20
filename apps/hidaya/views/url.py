import hashlib

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.utils import generate_signed_url


class GetSignedVideoURLView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, video_id, quality, file_name):
        key = request.data.get("key")
        if not key:
            return Response({"error": "Key is required"}, status=400)
        combined_key = f"{video_id}{quality}{file_name}"
        hashed_key = hashlib.sha256(combined_key.encode()).hexdigest()
        if key != hashed_key:
            return Response({"error": "Invalid key"}, status=400)
        path = f"/media/hls_videos/{video_id}/{quality}/{file_name}"
        signed_url = generate_signed_url(path, expiration=300)
        return Response(
            {
                "success": True,
                "message": "Signed URL generated successfully.",
                "data": {"signed_url": signed_url},
            }
        )

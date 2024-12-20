from rest_framework.response import Response
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.users.models import ActiveSessions


class CheckActiveSessionMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        """
        Middleware to check active sessions and update session information.
        """
        auth = JWTAuthentication()

        try:
            user_auth = auth.authenticate(request)
            if user_auth:
                user, token = user_auth
                fcm_token = request.headers.get("FCM-Token")
                session = ActiveSessions.objects.filter(
                    user=user, access_token=token
                ).first()
                if session:
                    if fcm_token:
                        session.fcm_token = fcm_token
                    session.save()
                    if not session.is_active:
                        return Response(
                            {
                                "success": False,
                                "message": "Invalid access token. Session is inactive.",
                            },
                            status=status.HTTP_401_UNAUTHORIZED,
                        )
                else:
                    return Response(
                        {
                            "success": False,
                            "message": "Session not found. Please log in again.",
                        },
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
        except AuthenticationFailed as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return None

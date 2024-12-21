from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
    MethodNotAllowed,
)
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):
        response.data = {"success": False, "message": "Incorrect authentication credentials."}

    elif isinstance(exc, NotAuthenticated):
        response.data = {
            "success": False,
            "message": "Authentication credentials were not provided.",
        }

    elif isinstance(exc, MethodNotAllowed):
        response.data = {"success": False, "message": "Method not allowed."}

    return response

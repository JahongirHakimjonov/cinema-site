from typing import Union

from rest_framework import exceptions
from rest_framework import status


class BreakException(Exception):
    """
    Break exception
    """

    def __init__(self, *args, message: Union[str, None] = None, data=None):
        if data is None:
            data = []
        self.args = args
        self.message = message
        self.data = data


class MyApiException(exceptions.APIException):
    """
    My API Exception for API exceptions status code edit
    """

    status_code = 400

    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class ResponseException:
    def __init__(
        self,
        message="",
        data=None,
        error_code=0,
        status_code=status.HTTP_400_BAD_REQUEST,
        exception=None,
        **kwargs,
    ):
        if isinstance(exception, BreakException):
            raise exception

        if data is None:
            data = []
        response = {
            "success": False,
            "message": message,
            "data": data,
            "error_code": error_code,
            **kwargs,
        }
        raise MyApiException(response, status_code)

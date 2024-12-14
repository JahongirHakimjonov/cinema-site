from apps.shared import exceptions
from apps.shared.exceptions import ResponseException
from apps.users.models import User
from apps.users.services import SmsService


class UserService(SmsService):
    @staticmethod
    def send_confirmation(self, phone) -> bool:
        try:
            self.send_confirm(phone)
            return True
        except exceptions.SmsException as e:
            ResponseException(e, data={"expired": e.kwargs.get("expired")})  # noqa
        except Exception as e:
            ResponseException(e)

    @staticmethod
    def change_password(self, phone, password):
        """
        Change password
        """
        user = User.objects.filter(phone=phone).first()
        user.set_password(password)
        user.save()

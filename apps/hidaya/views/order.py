from payme import Payme
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.choices import PaymentMethodChoices
from apps.hidaya.serializers import OrderSerializer
from core import settings

payme = Payme(payme_id=settings.PAYME_ID)


class OrderCreate(APIView):
    """
    API endpoint for creating an order.
    """

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a new order.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        result = {"order": serializer.data}

        if serializer.data["payment_method"] == PaymentMethodChoices.PAYME:
            payment_link = payme.initializer.generate_pay_link(
                id=serializer.data["id"],
                amount=serializer.data["total_price"],
                return_url=settings.PAYME_SUCCESS_URL,
            )
            payment_link = payment_link.replace(
                "https://checkout.paycom.uz/", settings.PAYME_CHECKOUT_URL
            )
            result["payment_link"] = payment_link

        return Response(result)

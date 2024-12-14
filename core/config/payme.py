import os

PAYME_ID = os.getenv("PAYME_ID")
PAYME_KEY = os.getenv("PAYME_KEY")
PAYME_ACCOUNT_FIELD = "id"  # maybe id key
PAYME_AMOUNT_FIELD = "total_price"
PAYME_ACCOUNT_MODEL = "apps.hidaya.models.Order"
PAYME_ONE_TIME_PAYMENT = True
PAYME_SUCCESS_URL = os.getenv("PAYME_SUCCESS_URL")
PAYME_CHECKOUT_URL = os.getenv("PAYME_CHECKOUT_URL")

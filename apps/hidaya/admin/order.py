from django.contrib import admin
from payme.models import PaymeTransactions
from unfold.admin import ModelAdmin

from apps.hidaya.models import Order

admin.site.unregister(PaymeTransactions)


@admin.register(PaymeTransactions)
class PaymeTransactionsAdmin(ModelAdmin):
    list_display = (
        "id",
        "transaction_id",
        "amount",
        "state",
        "created_at",
    )
    search_fields = ("transaction_id",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        "book",
        "user",
        "format",
        "payment_status",
        "total_price",
        "created_at",
    )
    search_fields = ("book", "user")
    autocomplete_fields = ("book", "user")
    readonly_fields = ("created_at", "updated_at")

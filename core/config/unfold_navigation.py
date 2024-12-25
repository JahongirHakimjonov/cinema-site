from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def user_has_group_or_permission(user, permission):
    if user.is_superuser:
        return True

    group_names = user.groups.values_list("name", flat=True)
    if not group_names:
        return True

    return user.groups.filter(permissions__codename=permission).exists()


PAGES = [
    {
        "seperator": True,
        "items": [
            {
                "title": _("Bosh sahifa"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Foydalanuvchilar"),
        "items": [
            {
                "title": _("Guruhlar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_group_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_group"
                ),
            },
            {
                "title": _("Foydalanuvchilar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:users_user_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
            {
                "title": _("Aktiv sesiyalar"),
                "icon": "visibility_lock",
                "link": reverse_lazy("admin:users_activesessions_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_activesessions"
                ),
            },
            {
                "title": _("SMS kodlar"),
                "icon": "sms",
                "link": reverse_lazy("admin:users_smsconfirm_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_smsconfirm"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Boshqaruv"),
        "items": [
            {
                "title": _("Kitoblar"),
                "icon": "menu_book",
                "link": reverse_lazy("admin:hidaya_book_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_book"
                ),
            },
            {
                "title": _("Videolar"),
                "icon": "play_circle",
                "link": reverse_lazy("admin:hidaya_video_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_video"
                ),
            },
            {
                "title": _("Yangiliklar"),
                "icon": "newspaper",
                "link": reverse_lazy("admin:hidaya_news_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_news"
                ),
            },
            {
                "title": _("Ma'lumotlar"),
                "icon": "info",
                "link": reverse_lazy("admin:hidaya_info_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_info"
                ),
            },
            {
                "title": _("Partnyorlar"),
                "icon": "handshake",
                "link": reverse_lazy("admin:hidaya_partner_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_partner"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Buyurtmalar"),
        "items": [
            {
                "title": _("Buyurtmalar"),
                "icon": "shopping_cart",
                "link": reverse_lazy("admin:hidaya_order_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_order"
                ),
            },
            {
                "title": _("To'lovlar"),
                "icon": "payments",
                "link": reverse_lazy("admin:payme_paymetransactions_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_paymetransactions"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Qo'shimcha"),
        "items": [
            {
                "title": _("Bildirishnomalar"),
                "icon": "notifications",
                "link": reverse_lazy("admin:hidaya_notification_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_notification"
                ),
            },
        ],
    },
]

TABS = [
    {
        "models": [
            "hidaya.book",
            "hidaya.genre",
            "hidaya.bookcategory",
        ],
        "items": [
            {
                "title": _("Kitoblar"),
                "link": reverse_lazy("admin:hidaya_book_changelist"),
            },
            {
                "title": _("Janrlar"),
                "link": reverse_lazy("admin:hidaya_genre_changelist"),
            },
            {
                "title": _("Kitob kategoriyalari"),
                "link": reverse_lazy("admin:hidaya_bookcategory_changelist"),
            },
        ],
    },
    {
        "models": [
            "hidaya.video",
            "hidaya.tags",
            "hidaya.videocategory",
        ],
        "items": [
            {
                "title": _("Videolar"),
                "link": reverse_lazy("admin:hidaya_video_changelist"),
            },
            {
                "title": _("Video turlari"),
                "link": reverse_lazy("admin:hidaya_tags_changelist"),
            },
            {
                "title": _("Video kategoriyalari"),
                "link": reverse_lazy("admin:hidaya_videocategory_changelist"),
            },
        ],
    },
    {
        "models": [
            "hidaya.news",
            "hidaya.newscategory",
        ],
        "items": [
            {
                "title": _("Yangiliklar"),
                "link": reverse_lazy("admin:hidaya_news_changelist"),
            },
            {
                "title": _("Yangilik kategoriyalari"),
                "link": reverse_lazy("admin:hidaya_newscategory_changelist"),
            },
        ],
    },
]

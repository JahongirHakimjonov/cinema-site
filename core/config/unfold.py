import os

from django.templatetags.static import static

# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse_lazy
from . import unfold_navigation as navigation


def environment_callback(request):  # noqa
    """
    Callback has to return a list of two values represeting text value and the color
    type of the label displayed in top right corner.
    """
    return [os.getenv("STATUS"), "success"]  # info, danger, warning, success


UNFOLD = {
    "SITE_TITLE": "Django Default",
    "SITE_HEADER": "Django Default",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("images/django-logo.webp"),
        "dark": lambda request: static("images/django-logo.webp"),
    },
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/icon",
            "href": lambda request: static("images/favicon.ico"),
        },
    ],
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_LANGUAGES": True,
    "ENVIRONMENT": "core.config.unfold.environment_callback",
    "LOGIN": {
        "image": lambda request: static("images/login.webp"),
    },
    "STYLES": [
        lambda request: static("css/tailwind.css"),
    ],
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "0 104 56",
            "100": "0 104 56",
            "200": "0 104 56",
            "300": "0 104 56",
            "400": "0 104 56",
            "500": "0 104 56",
            "600": "0 104 56",
            "700": "0 104 56",
            "800": "0 104 56",
            "900": "0 104 56",
            "950": "0 104 56",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "uz": "🇺🇿",
                "en": "🇬🇧",
                "ko": "🇺🇿",
                "tr": "🇹🇷",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": navigation.PAGES,
    },
    "TABS": navigation.TABS,
}

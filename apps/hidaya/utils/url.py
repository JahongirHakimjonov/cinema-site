import hashlib
import hmac
import time

from core import settings

SECRET_KEY = settings.SECRET_KEY


def generate_signed_url(path, expiration=10):
    """
    Imzolangan URL yaratadi.

    :param path: Foydalanuvchi kirishi kerak bo‘lgan yo‘l (masalan: '/media/hls_videos/3/1080p/playlist.m3u8')
    :param expiration: URL amal qilish vaqti (soniyalar)
    :return: Imzolangan URL
    """
    expires_at = int(time.time()) + expiration  # Hozirgi vaqt + amal qilish muddati
    message = f"{path}{expires_at}"  # Yo‘l va muddati birlashtiriladi
    signature = hmac.new(
        SECRET_KEY.encode(), message.encode(), hashlib.sha256
    ).hexdigest()  # Imzo yaratiladi
    signed_url = f"{path}?expires={expires_at}&signature={signature}"
    return signed_url

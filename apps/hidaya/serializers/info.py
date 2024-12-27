from urllib.parse import urljoin

from bs4 import BeautifulSoup
from django.conf import settings
from rest_framework import serializers

from apps.hidaya.models import Info


class InfoSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ("id", "title", "description", "created_at")

    def get_description(self, obj):
        base_url = settings.SITE_DOMAIN
        soup = BeautifulSoup(obj.description, 'html.parser')

        for img in soup.find_all('img', src=True):
            img['src'] = urljoin(base_url, img['src'])

        for a in soup.find_all('a', href=True):
            a['href'] = urljoin(base_url, a['href'])

        return str(soup)

from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.hidaya.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        widgets = {
            "description": CKEditor5Widget(),
        }
        fields = "__all__"

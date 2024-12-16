from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import Video


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ("title", "description")

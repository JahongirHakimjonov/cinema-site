from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import Info


@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ("title", "description")

from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import Partner


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ("name",)

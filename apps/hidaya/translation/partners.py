from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import Partner, Platform


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Platform)
class PlatformTranslationOptions(TranslationOptions):
    fields = ("title", "description", "text")
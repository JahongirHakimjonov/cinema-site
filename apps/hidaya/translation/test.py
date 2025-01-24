from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import Question, Answer


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ("question",)


@register(Answer)
class AnswerTranslationOptions(TranslationOptions):
    fields = ("answer",)

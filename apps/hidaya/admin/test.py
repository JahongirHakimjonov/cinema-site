from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, StackedInline

from apps.hidaya.models import Question, Answer


class AnswerInline(StackedInline):
    model = Answer
    extra = 1
    tab = True
    fields = ("answer_uz", "answer_tr", "answer_en", "answer_ko", "ball", "is_correct")


@admin.register(Question)
class QuestionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "book", "question", "is_active")
    list_filter = ("is_active",)
    search_fields = ("question",)
    inlines = (AnswerInline,)
    autocomplete_fields = ("book",)


@admin.register(Answer)
class AnswerAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "answer", "ball", "is_correct")
    list_filter = ("is_correct",)
    search_fields = ("answer",)
    autocomplete_fields = ("question",)

from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from apps.hidaya.models import Question, Answer


class AnswerInline(TabularInline):
    model = Answer
    extra = 1


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'book', 'question', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('question',)
    inlines = (AnswerInline,)
    autocomplete_fields = ('book',)


@admin.register(Answer)
class AnswerAdmin(ModelAdmin):
    list_display = ('id', 'answer', 'ball', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('answer',)
    autocomplete_fields = ('question',)

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Question(AbstractBaseModel):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='questions')
    question = models.TextField(verbose_name=_('Question'))
    is_active = models.BooleanField(verbose_name=_('Is active'), default=True)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ('-created_at',)
        db_table = 'question'

    def __str__(self):
        return self.question


class Answer(AbstractBaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField(verbose_name=_('Answer'))
    ball = models.IntegerField(verbose_name=_('Ball'), default=0)
    is_correct = models.BooleanField(verbose_name=_('Is correct'), default=False)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ('-created_at',)
        db_table = 'answer'

    def __str__(self):
        return self.answer

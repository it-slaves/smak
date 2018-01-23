from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.constants import GRADES, SUBJECTS, SCALE_ANSWERS


class Poll(models.Model):
    name = models.CharField(
        max_length=30,
        null=True
    )
    subject = models.CharField(
        max_length=100,
        choices=SUBJECTS,
        help_text=_('Subject polls prepared for')
    )
    grade = models.IntegerField(
        choices=GRADES,
        help_text=_('Grade polls prepared for')
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(
        'polls.Poll',
        on_delete=models.CASCADE,
        help_text=_('Poll question belongs to')
    )
    question = models.CharField(
        max_length=100,
        help_text=_('Question text')
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return str(self.poll) + '_' + str(self.question[:20]).replace(' ', '_')


class Answer(models.Model):
    question = models.ForeignKey(
        'polls.Question',
        on_delete=models.CASCADE,
        help_text=_('Question answers refers to')
    )
    student = models.ForeignKey(
        'accounts.Student',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        help_text=_('The student who answered')
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return str(self.question) + str(self.student)


class ScaleAnswer(Answer):
    answer = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=SCALE_ANSWERS,
        help_text=_('Scale answer for question')
    )

    class Meta:
        verbose_name = 'Ответ по шкале'
        verbose_name_plural = 'Ответы по шкале'


class TextAnswer(Answer):
    answer = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text=_('Text answer for question')
    )

    class Meta:
        verbose_name = 'Текстовый ответ'
        verbose_name_plural = 'Текстовые ответы'

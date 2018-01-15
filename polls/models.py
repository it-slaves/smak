from django.db import models
from accounts.constants import GRADES, SUBJECTS, ANSWERS
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
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
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __str__(self):
        return str(self.subject) + '_' + str(self.grade)


class Question(models.Model):
    poll = models.ForeignKey(
        'polls.Poll',
        help_text=_('Poll question belongs to'),
        on_delete=models.CASCADE
    )
    question = models.CharField(
        max_length=100,
        help_text=_('Question text')
    )
    answer = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=ANSWERS,
        help_text=_('Learner answer')
    )

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return str(self.poll) + '_' + str(self.question[:20]).replace(' ', '_')

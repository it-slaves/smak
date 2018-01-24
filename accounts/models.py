from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .constants import GRADES


class Director(User):
    def __str__(self):
        return ' '.join((self.first_name, self.last_name, self.patronymic, self.username))

    pic = models.ImageField(
        blank=True,
        null=True,
        upload_to='director_photos',
        help_text=_('Profile photo'),
    )
    link = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        unique=True,
        help_text=_('Link for students to register')
    )
    patronymic = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name=_('Отчество'),
        help_text=_('Directors patronymic')
    )

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директора'


class Student(User):
    def __str__(self):
        return ' '.join((self.first_name, self.last_name, self.patronymic, self.username))

    school_director = models.ForeignKey(
        'accounts.Director',
        blank=True,
        null=True,
        help_text=_('Director student refers to'),
        on_delete=models.CASCADE
    )
    grade = models.IntegerField(
        choices=GRADES,
        default=11,
        help_text=_('Students grade in school')
    )
    polls = models.ManyToManyField(
        'polls.Poll',
        blank=True,
        null=True,
        help_text=_('Polls to answer'),
    )
    patronymic = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text=_('Students patronymic')
    )

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


def get_director(self):
    try:
        return Director.objects.get(pk=self.pk)
    except Director.DoesNotExist:
        return None


def get_student(self):
    try:
        return Student.objects.get(pk=self.pk)
    except Student.DoesNotExist:
        return None


User.add_to_class('get_director', get_director)
User.add_to_class('get_student', get_student)

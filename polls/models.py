import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    principal = models.ForeignKey(User)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subject(models.Model):
    poll = models.ForeignKey(Poll)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
    # pub_date = models.DateTimeField('date published')
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'


class Answer(models.Model):
    student = models.ForeignKey(User)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)


class Comment(models.Model):
    student = models.ForeignKey(User)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.CharField(max_length=500)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer_text = models.CharField(max_length=300)

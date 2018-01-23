import json

from django.http import HttpResponse
from rest_framework import status

from .models import Poll, Question


def get_polls(request):
    polls = []
    for poll in Poll.objects.all():
        questions = []
        for question in Question.objects.filter(poll=poll.pk):
            questions.append({'id': question.id, 'text': question.question})

        polls.append({'id': poll.id, 'name': poll.name, 'questions': questions})

    return HttpResponse(status=status.HTTP_200_OK,
                        content=json.dumps({'polls': polls}),
                        content_type='application/json')

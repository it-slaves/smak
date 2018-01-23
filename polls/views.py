import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

from accounts.models import Student
from .models import Poll, Question, ScaleAnswer, TextAnswer


@api_view(['GET'])
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


@api_view(['POST'])
def submit_answers(request):
    # TODO: change student id by taking it from request.user
    student = Student.objects.get(pk=3)
    answers = json.loads(request.body)['answers']
    for answer in answers:
        question = Question.objects.get(pk=answer['question'])
        if answer['scale']:
            ScaleAnswer.objects.create(student=student,
                                       question=question,
                                       answer=answer['answer'])
        else:
            TextAnswer.objects.create(student=student,
                                      question=question,
                                      answer=answer['answer'])

    return HttpResponse(status.HTTP_200_OK)

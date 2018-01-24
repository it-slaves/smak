import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

from accounts.models import Student
from .models import Poll, Question, ScaleAnswer, TextAnswer


@api_view(['GET'])
def get_polls(request):
    # TODO: change student id by taking it from request.user
    student = Student.objects.get(pk=3)
    polls = []
    for poll in Poll.objects.all():
        if poll in student.polls.all():
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
    polls = json.loads(request.body)['polls']
    for poll in polls:
        answers = poll['answers']
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
        student.polls.remove(Poll.objects.get(pk=poll['id']))

    return HttpResponse(status.HTTP_200_OK)

from django.contrib import admin

from polls.models import Poll, Question, ScaleAnswer, TextAnswer

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(ScaleAnswer)
admin.site.register(TextAnswer)

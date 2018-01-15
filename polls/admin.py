from django.contrib import admin

from polls.models import Poll, Question

admin.site.register(Poll)
admin.site.register(Question)

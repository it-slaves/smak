from django.contrib import admin

from .models import Subject, Poll, Question, Answer, Comment, Choice
from django.contrib.auth.models import User


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 5

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 5

class PollAdmin(admin.ModelAdmin):
    inlines = [SubjectInline, QuestionInline]    

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     # list_display = ('question_text', 'pub_date', 'was_published_recently')
#     # list_filter = ['pub_date']
#     search_fields = ['question_text']

# class PollAdmin(admin.ModelAdmin):

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
admin.site.register(Poll, PollAdmin)
# admin.site.register(Subject)
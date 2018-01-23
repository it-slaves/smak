from django.conf.urls import url

from .views import get_polls, submit_answers

urlpatterns = [
    url(r'^get_polls/', get_polls, name='get_polls'),
    url(r'^submit_answers/', submit_answers, name='get_answers'),
]

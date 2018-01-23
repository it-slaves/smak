from django.conf.urls import url

from .views import get_polls

urlpatterns = [
    url(r'^get_polls/', get_polls, name='get_polls'),
]

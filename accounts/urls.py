from django.conf.urls import url
from django.contrib.auth.views import login, logout

from accounts.forms import UserAuthenticationForm
from accounts.views import register_director, register_student, profile

urlpatterns = [
    url(r'^$', login, {'template_name': 'accounts/login.html',
                       'authentication_form': UserAuthenticationForm}, name='login'),
    url(r'^logout/', logout, {'next_page': '/'}),
    url(r'^profile/', profile, name='profile'),
    url(r'^register_director/', register_director, name='register_director'),
    url(r'^register_student/', register_student, name='register_student'),
]

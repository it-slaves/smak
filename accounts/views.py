import string

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from accounts.forms import DirectorRegistrationForm, StudentRegistrationForm
from accounts.models import Director
from polls.models import Poll


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'accounts/profile.html')


def register_director(request):
    """
    Register director view
    Renders registration form or creates new director object and redirect to his profile
    Creates directors special (unique) link for students to register to refer to this director. Pattern: dir + [A-Z]{5}
    """
    if request.method == 'POST':
        form = DirectorRegistrationForm(request.POST)
        if form.is_valid():
            director = form.save()
            director.link = 'dir' + get_random_string(length=5, allowed_chars=string.ascii_uppercase)
            director.save()
            director = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, director)
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = DirectorRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form, 'is_director': True})


def register_student(request):
    """
    Register student view
    Precondition: directors id must be stored in session
    Renders registration form or creates new student object and redirect to his profile
    Associates student with director with id stored in session
    Adds all existed polls from database to students polls list
    """
    director_id = request.session['director_id']
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            try:
                student.school_director = Director.objects.get(pk=director_id)
                for poll in Poll.objects.all():
                    student.polls.add(poll)
                student.save()
            except Director.DoesNotExist:
                # TODO: show error to HTML form
                print('Director does not exists')
            student = authenticate(username=form.cleaned_data['username'],
                                   password=form.cleaned_data['password1'])
            login(request, student)
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = StudentRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form, 'is_director': False})


def redirect_student(request):
    """
    Redirects student from pattern link /dir + [A-Z]{5} to registration view
    Depend on directors link stores director id in session
    """
    director_link = request.path.replace('/', '')
    request.session['director_id'] = Director.objects.get(link=director_link).id
    return redirect(register_student)

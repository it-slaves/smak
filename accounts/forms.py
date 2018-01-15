from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from accounts.constants import GRADES
from .models import Director, Student


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

    # Username = email
    username = forms.EmailField(
        label=_('Адрес электронной почты'),
        widget=forms.EmailInput(),
        help_text=_('Enter your email')
    )
    first_name = forms.CharField(
        label=_('Имя'),
        max_length=30,
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        label=_('Фамилия'),
        max_length=30,
        widget=forms.TextInput()
    )
    patronymic = forms.CharField(
        label=_('Отчество'),
        max_length=30,
        widget=forms.TextInput()
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.patronymic = self.cleaned_data['patronymic']

        if commit:
            user.save()
        return user


class DirectorRegistrationForm(UserRegistrationForm):
    def __init__(self, *args, **kwargs):
        super(DirectorRegistrationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Director
        fields = ('first_name', 'last_name', 'patronymic', 'username', 'password1', 'password2')


class StudentRegistrationForm(UserRegistrationForm):
    # TODO: fix grade field (registration doesnt work)
    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)

    # grade = forms.ChoiceField(
    #     label=_('Класс'),
    #     choices=GRADES,
    #     widget=forms.NumberInput()
    # )

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'patronymic', 'username', 'password1', 'password2',)

    def save(self, commit=True):
        student = super().save(commit=False)
        # student.grade = self.cleaned_data['grade']
        if commit:
            student.save()
        return student


class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(
        label=_('Адрес электронной почты'),
        widget=forms.EmailInput(),
        help_text=_('Enter your email')
    )
    password = forms.CharField(
        label=_('Пароль'),
        max_length=30,
        widget=forms.PasswordInput()
    )

    class Meta:
        fields = ('username', 'password')

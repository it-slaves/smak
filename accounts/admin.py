from django.contrib import admin

from django.contrib.auth.models import Group, User
from .models import Director, Student


admin.site.unregister(Group)

admin.site.register(Director)
admin.site.register(Student)

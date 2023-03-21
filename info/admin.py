from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

admin.site.register(Teacher)
#admin.site.register(Group)
admin.site.register(Discipline)
admin.site.register(Lesson)
admin.site.register(Room)
admin.site.register(Position)
admin.site.register(Education)
admin.site.register(LessonType)
admin.site.unregister(Group)

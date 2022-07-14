from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Habit, Tracker, Frequency

# Register your models here.
admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Tracker)
admin.site.register(Frequency)

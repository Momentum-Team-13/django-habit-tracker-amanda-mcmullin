from django.contrib import admin
from .models import User, Habit, HabitTracker
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User)
admin.site.register(Habit)
admin.site.register(HabitTracker)
# admin.site.register(UserAdmin)
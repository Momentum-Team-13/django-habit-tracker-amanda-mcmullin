from django import forms
from .models import User, Habit, HabitTracker

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'user_name',
            'email',
        ]


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'creator',
            'habit_name',
            'goal',
            'unit',
        ]


class HabitTrackerForm(forms.ModelForm):
    class Meta:
        model = HabitTracker
        fields = [
            'habit',
            'goal_quantity',
        ]
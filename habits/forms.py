from django import forms
from .models import  Habit, HabitTracker


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
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


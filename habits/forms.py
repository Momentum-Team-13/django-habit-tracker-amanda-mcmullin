from django import forms
from .models import BaseModel, Habit, HabitTracker

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
            'note',
        ]
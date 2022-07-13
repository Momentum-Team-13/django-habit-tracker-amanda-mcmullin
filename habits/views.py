from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitTracker
from .forms import HabitForm, HabitTrackerForm

# Create your views here.
def home(request):
    habits = Habit.objects.all()
    return render(request, "Habits/list_habits.html", {'habits': habits})
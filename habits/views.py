from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitTracker
from .forms import HabitForm, HabitTrackerForm

# Create your views here.
def home(request):
    habits = Habit.objects.all()
    return render(request, "habits/home.html")

def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    return render(request, "habits/edit_habit.html", {
        "form": form,
    "habit": habit
})


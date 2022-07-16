from http.client import REQUEST_ENTITY_TOO_LARGE
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Habit
from .forms import HabitForm, HabitTrackerForm


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('habits_list')
    return render(request, 'habits/home.html')


@login_required
def habits_list(request):
    habit = Habit.objects.all()
    return render(request, 'Habits/habits_list.html', {'habit': habit})


@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'habits/habit_detail.html', {"habit": habit})


@login_required
def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your new habit has been added!")
            return redirect(to='habits_list')
    return render(request, "habits/add_habit.html", {"form": form})


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='habits_list')
    return render(request, "habits/delete_habit.html", {"habit": habit})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to="habits_list")
    return render(request, "habits/edit_habit.html", 
        {"form": form, "habit": habit})


@login_required
def add_entry(request, pk):
    habit = get_object_or_404(Habit, pk=pk )
    if request.method == "POST":
        form = HabitTrackerForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.habit = habit
            entry.save()
            return redirect(to='habit_detail', pk=habit.pk)
        else:
            form = HabitTrackerForm()
        return render(request, "habits/add_entry.html", {"form": form, "habit": habit})






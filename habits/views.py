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
    habits = Habit.objects.all()
    return render(request, 'habits/habits_list.html', {'habits': habits})


@login_required
def habit_detail(request, pk):
    habits = Habit.objects.all()
    habit = get_object_or_404(habits, pk=pk)
    return render(request, 'habits/habit_detail.html', {"habit": habit})


@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, "Your new habit has been added!")
            return redirect(to='habits_list', pk=habit.pk)
        else:
            form = HabitForm()
    return render(request, "habits/add_habit.html", {"form": form})


@login_required
def delete_habit(request, pk):
    habits = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habits.delete()
        return redirect(to='habits_list')
    return render(request, "habits/delete_habit.html", {"habits": habits})


@login_required
def edit_habit(request, pk):
    habits = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        forms = HabitForm(instance=habits)
    else:
        forms = HabitForm(data=request.POST, instance=habits)
        if forms.is_valid():
            forms.save()
            return redirect(to="habit_detail")
    return render(request, "habits/edit_habit.html", 
        {"forms": forms, "habits": habits})


@login_required
def add_entry(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk )
    if request.method == "POST":
        form = HabitTrackerForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.habit = habit
            entry.save()
            return redirect(to='habit_detail', pk=habit.pk)
        else:
            form = HabitTrackerForm()
        return render(request, "habits/add_entry.html", {"form": form})






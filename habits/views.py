from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Habit, HabitTracker
from .forms import HabitForm, HabitTrackerForm
import datetime


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('habits_list')
    return render(request, 'habits/home.html')


@login_required
def habits_list(request):
    habits = Habit.objects.filter(creator=request.user.pk)
    date = {
        'year': datetime.date.today().year,
        'month': datetime.date.today().month,
        'day': datetime.date.today().day,
    }
    return render(request, 'habits/habits_list.html', {'creator': request.user, 'habits': habits, 'date': date})


@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.creator = request.user
            habit.save()
            messages.success(request, "Your new habit has been added!")
            return redirect("habit_detail", pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, "habits/add_habit.html", {"form": form})


@login_required
def update_create_tracker (request, pk, year, month, day):
    user_habit = Habit.objects.filter(creator=request.user.pk).get(Habit, pk=pk)
    record_date = datetime.date(year, month, day)

    if request.method == "POST":
        target = request.POST.get('goal_quantity')
        record, _ = HabitTracker.objects.get_or_create(date=record_date, habit=user_habit)
        record.goal_quantity = target
        record.save()
        return redirect("details_habit", pk=user_habit.pk)
    else:
        records = HabitTracker.objects.filter(date=record_date, habit=user_habit)
        if records.exists():
            form = HabitTrackerForm(instance=records[0])
        else:
            form = HabitTrackerForm()

    return render(
        request, "habits/update_create_tracker.html",
        {"form": form, "habit": user_habit}
    )


@login_required
def habit_detail(request, pk):
        user_habit = Habit.objects.filter(creator=request.user.pk).get(pk=pk)
        user_records = HabitTracker.objects.filter(habit=user_habit).order_by('-date')
        date = {
            'year': datetime.date.today().year,
            'month': datetime.date.today().month,
            'day': datetime.date.today().day
        }
        return render(request, "habits/habit_detail.html", {
            "habit": user_habit,
            "date": date,
            "user_records": user_records
        })

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
    return render(request, 'habits/habits_list.html', {'user': request.user, 'habits': habits, 'date': date})

# @login_required
# def habits_list(request):
#     habit = Habit.objects.filter(user=request.user.pk)
#     return render(request, 'Habits/habits_list.html', {'habit': habit})


@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, "Your new habit has been added!")
            return redirect("habit_detail", pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, "habits/add_habit.html", {"form": form})


@login_required
def update_create_tracker (request, pk, year, month, day):
    user_habit = Habit.objects.filter(user=request.user.pk).get(pk=pk)
    record_date = datetime.date(year, month, day)

    if request.method == "POST":
        target = request.POST.get('goal_quantity')
        record, _ = HabitTracker.objects.get_or_create(date=record_date, habit=user_habit)
        record.daily_number = target
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

# @login_required
# def habit_detail(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)
#     return render(request, 'habits/habit_detail.html', {"habit": habit})

#     # if request.method == 'GET':
#     #     form = HabitForm()
#     # else:
#     #     form = HabitForm(data=request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.success(request, "Your new habit has been added!")
#     #         return redirect(to='habits_list')
#     # return render(request, "habits/add_habit.html", {"form": form})



# @login_required
# def delete_habit(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)
#     if request.method == 'POST':
#         habit.delete()
#         return redirect(to='habits_list')
#     return render(request, "habits/delete_habit.html", {"habit": habit})


# @login_required
# def edit_habit(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)
#     if request.method == "GET":
#         form = HabitForm(instance=habit)
#     else:
#         form = HabitForm(data=request.POST, instance=habit)
#         if form.is_valid():
#             form.save()
#             return redirect(to="habits_list")
#     return render(request, "habits/edit_habit.html", 
#         {"form": form, "habit": habit})


# @login_required
# def add_entry(request, pk):
#     habit = get_object_or_404(Habit, pk=pk )
#     if request.method == "POST":
#         form = HabitTrackerForm(data=request.POST)
#         if form.is_valid():
#             entry = form.save(commit=False)
#             entry.habit = habit
#             entry.save()
#             return redirect(to='habit_detail', pk=habit.pk)
#         else:
#             form = HabitTrackerForm()
#         return render(request, "habits/add_entry.html", {"form": form, "habit": habit})

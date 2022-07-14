from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('habit_list')
    return render(request, 'habits/home.html')


@login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request,'habits/habit_list.html', {'habits': habits})

@login_required
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

@login_required
def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            new_habit = form.save(commit=False)
            new_habit.user = request.user
            new_habit.save()
            return redirect(to='/habit_list')
    return render(request, "habits/add_habit.html", {"form": form})


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='habit_list')
    return render(request, "habits/delete_habit.html", {"habit": habit})
        
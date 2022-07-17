from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm, TrackerForm


# Create your views here.
def main(request):
    if request.user.is_authenticated:
        return redirect('habit_list')
    return render(request, 'habits/main.html')


@login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, "habits/habit_list.html", {"habits": habits})


def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            new_habit = form.save(commit=False)
            new_habit.user = request.user
            new_habit.save()
            return redirect(to='habit_list')

    return render(request, "habits/add_habit.html", {"form": form})


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = TrackerForm()
    else:
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.habit = habit
            habit.save()
            return redirect(to='habit_detail', pk=pk)

    return render(request, "habits/habit_detail.html", {"form": form,
                  "habit": habit})

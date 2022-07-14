from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm


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
            form.save()
            return redirect(to='habit_list')

    return render(request, "habits/add_habit.html", {"form": form})

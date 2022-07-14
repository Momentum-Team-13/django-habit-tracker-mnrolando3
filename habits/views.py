from django.shortcuts import get_object_or_404, render, redirect
from .models import Habit, Tracker, User
from .forms import HabitForm


# Create your views here.
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, "habits/habit_list.html", {"habits": habits})


# def add_habit(request):
#     if request.method == 'GET':
#         form = HabitForm()
#     else:
#         form = HabitForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='habit_list')

#     return render(request, "habits/add_habit.html", {"form": form})

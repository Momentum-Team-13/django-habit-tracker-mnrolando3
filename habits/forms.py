from django import forms
from .models import Habit, Tracker


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'title',
            'description',
            'goal',
            'frequency',
        ]


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = [
            'add_record',
        ]

from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username} {self.email}'


class Frequency(models.Model):
    frequency = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.frequency}'


class Habit(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    goal = models.PositiveIntegerField()
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE,
                                  related_name='freq_habits', null=True,
                                  blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_habits')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title} {self.description}'


class Tracker(models.Model):
    add_record = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE,
                              related_name='trackers')

    def __str__(self):
        return f'{self.add_record}{self.updated_at}'

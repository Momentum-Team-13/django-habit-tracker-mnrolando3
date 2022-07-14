from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    pass

    def __str__(self):
        return f'{self.username} {self.email}'

class Habit(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    goal = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='habits')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title} {self.description}'


class Tracker(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE,
                              related_name='trackers')
    quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.updated_at}'

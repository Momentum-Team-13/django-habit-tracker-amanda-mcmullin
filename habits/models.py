from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 


class Habit(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    goal = models.IntegerField(default=0)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="habits")

    def __str__(self):
        return f"Title: {self.title} / Description: {self.description} / Goal: {self.goal}"


class HabitTracker(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="habit_trackers")
    date = models.DateField(default=datetime.date.today)
    tracking_unit = models.IntegerField(default=0)

    def __str__(self):
        return f"Date: {self.date} / Amount Completed: {self.tracking_unit}"

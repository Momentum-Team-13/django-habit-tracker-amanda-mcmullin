from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    # user_name = models.CharField(max_length=100, null=True, blank=True)
    # email = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return f"User Name : {self.user_name} | Email: {self.email}" 
    def __str__(self):
        return self.username


class Habit(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    name = models.CharField(max_length=150)
    description = models.TextField
    goal = models.IntegerField(default=0)
    unit = models.CharField(max_length=55)

    def __str__(self):
        return f"Name: {self.name} | Description: {self.description} | Goal: {self.goal} | Unit: {self.unit}"


class HabitTracker(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="habit_trackers")
    date = models.DateField(default=datetime.date.today)
    tracking_goal = models.IntegerField(default=0)
    note = models.TextField

    def __str__(self):
        return f"Date: {self.date} | Amount Completed: {self.tracking_goal} | Note: {self.note}"


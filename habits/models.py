from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
import datetime

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    def __str__(self):
        return self.username


class Habit(BaseModel):
    creator = models.ForeignKey("User", on_delete=models.CASCADE, related_name="habits")
    habit_name = models.CharField(max_length=150)
    goal = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=55)

    def __str__(self):
        return f"Name: {self.habit_name} | Goal: {self.goal} | Unit: {self.unit}"


class HabitTracker(BaseModel):
    habit = models.ForeignKey("Habit", on_delete=models.CASCADE, related_name="habit_trackers")
    date = models.DateField(default=datetime.date.today)
    goal_quantity = models.PositiveIntegerField(default=0)
    note = models.TextField(null=True, blank=True)
    note_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_habit_date')
        ]

    def __str__(self):
        return f"Date: {self.date} | Amount Completed: {self.goal_quantity} | Note: {self.note}"


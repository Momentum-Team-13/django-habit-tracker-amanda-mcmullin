from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    def __str__(self):
        return self.username


class Habit(BaseModel):
    creator = models.ForeignKey("User", on_delete=models.CASCADE, related_name="habits")
    habit_name = models.CharField(max_length=150)
    goal = models.PositiveIntegerField()
    unit = models.CharField(max_length=55)

    def __str__(self):
        return f"Name: {self.habit_name} | Goal: {self.goal} | Unit: {self.unit}"


class HabitTracker(BaseModel):
    habit = models.ForeignKey("Habit", on_delete=models.CASCADE, related_name="habittrackers")
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    goal_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.date

    class Meta:
        verbose_name_plural = 'HabitTrackers'
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_entry')
        ]

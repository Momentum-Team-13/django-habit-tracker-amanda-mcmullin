from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Profile(models.Model):
    pass


class Habit(models.Model):
    pass

class HabitTracker(models.Model):
    pass

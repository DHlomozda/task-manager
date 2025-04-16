from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)


class TaskType(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"


class Task(models.Model):
    class Priority(models.TextChoices):
        URGENT = "Urgent", "Urgent"
        HIGH = "High", "High"
        MEDIUM = "Medium", "Medium"
        LOW = "Low", "Low"

    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=50, choices=Priority.choices, default=Priority.LOW)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

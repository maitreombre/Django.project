from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    LEVELS = [
        ("Default", "Default"),
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    ]

    title = models.CharField(max_length=30, verbose_name='Task name')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Task description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    due_date = models.DateTimeField(blank=True, null=True, verbose_name='Deadline')
    completed = models.BooleanField(default=False, verbose_name='The task is completed')
    priority = models.CharField(max_length=15, choices=LEVELS, default='Default', verbose_name='Priority value')
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, default=None)


class Friend(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    date_added = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    comment = models.TextField(blank=True, null=True, verbose_name='Comment to task')
    task = models.ForeignKey('Task', on_delete=models.CASCADE, default=None, related_name='comments')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None,  related_name='creator')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')


class CommonTask(Task):

    shared_with = models.ManyToManyField(User, related_name='tasks_participated')






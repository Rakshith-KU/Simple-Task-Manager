from django.db import models
from django.contrib.auth.models import User  # to connect each task to a user

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link task to a user
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

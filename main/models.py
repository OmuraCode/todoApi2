from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
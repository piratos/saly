from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


status_choices = (
    ('stuck', 'stuck'),
    ('in progress', 'in progress'),
    ('done', 'done'),
    ('canceled', 'canceled'),)

project_choices = (
    ('active', 'active'),
    ('archived', 'archived'),)

class Project(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)
    status = models.CharField(max_length=128, choices=project_choices, default='active')
    def __str__(self):
        return self.name

class ToDoTask(models.Model):
    name = models.CharField(max_length=256)
    priority = models.IntegerField(default=0)
    note = models.TextField(blank=True)
    status = models.CharField(choices=status_choices, max_length=128, default='stuck')
    project = models.ForeignKey(Project)
    def __str__(self):
        return self.name

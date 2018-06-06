from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


status_choices = (
	('stuck', 'stuck'),
	('in progress', 'in progress'),
	('done', 'done'),
	('canceled', 'canceled'))

class ToDoTask(models.Model):
	name = models.CharField(max_length=256)
	user = models.ForeignKey(User)
	priority = models.IntegerField(default=0)
	note = models.TextField(blank=True)
	status = models.CharField(choices=status_choices, max_length=128, default='stuck')

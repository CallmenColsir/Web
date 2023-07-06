from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class TodoItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)


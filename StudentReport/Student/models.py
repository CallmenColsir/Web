from django.db import models


class StudentData(models.Model):
    name = models.CharField(max_length=64, blank=False, null=True)
    age = models.IntegerField(blank=False, null=True)
    major = models.CharField(max_length=6, blank=False, null=True)
    
    def __str__(self):
        return self.name

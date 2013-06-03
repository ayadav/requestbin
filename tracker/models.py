from django.db import models
from datetime import datetime

class Issue(models.Model):
    """Models an individual issue"""
    notes = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())

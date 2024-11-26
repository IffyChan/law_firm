from django.db import models

class CourtSession(models.Model):
    case_name = models.CharField(max_length=200)
    start_time = models.DateTimeField()

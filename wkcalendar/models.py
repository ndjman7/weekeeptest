from django.db import models

class schedule(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    day = models.CharField(max_length=10)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)

    def __str__(self):
        return self.title

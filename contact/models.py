from django.db import models
from django.utils import timezone
# Create your models here.

class Contact (models.Model):
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.firts_name} {self.last_name}'
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Vacation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    weather_conditions = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('vacation-detail', kwargs={'vacation_id': self.id})

STAR_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

class Star(models.Model):
    #choose from selected stars
    star = models.CharField('Stars', max_length=1, choices=STAR_CHOICES)
    rating = models.TextField(max_length=250)

    vacation = models.ForeignKey(Vacation, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.star} stars"
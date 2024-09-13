from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    food_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'restaurant_id': self.id})
    
class Star(models.Model):
    star = models.IntegerField('Stars')
    rating = models.TextField(max_length=250)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} stars"
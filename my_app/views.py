from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Restaurant
from .forms import StarForm

class RestaurantCreate(CreateView):
    model = Restaurant
    fields = '__all__'
    success_url = '/restaurants/'

class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = '__all__'

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = '/restaurants/'

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    star_form = StarForm()
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant, 'star_form': star_form})

def add_stars(request, restaurant_id):
    form = StarForm(request.POST)
    if form.is_valid():
        new_star = form.save(commit=False)
        new_star.restaurant_id = restaurant_id
        new_star.save()
    return redirect('restaurant-detail', restaurant_id=restaurant_id)
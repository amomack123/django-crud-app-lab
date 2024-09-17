from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Restaurant
from .forms import StarForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = '__all__'
    success_url = '/restaurants/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RestaurantUpdate(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = '__all__'

class RestaurantDelete(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = '/restaurants/'

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

@login_required
def restaurants(request):
    restaurants = Restaurant.objects.filter(user=request.user)
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

@login_required
def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    star_form = StarForm()
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant, 'star_form': star_form})

@login_required
def add_stars(request, restaurant_id):
    form = StarForm(request.POST)
    if form.is_valid():
        new_star = form.save(commit=False)
        new_star.restaurant_id = restaurant_id
        new_star.save()
    return redirect('restaurant-detail', restaurant_id=restaurant_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('restaurants')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
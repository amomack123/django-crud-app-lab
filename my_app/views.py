from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vacation
from .forms import StarForm
from .forms import VacationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

class VacationCreate(LoginRequiredMixin, CreateView):
    model = Vacation
    fields = '__all__'
    success_url = '/vacations/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VacationUpdate(LoginRequiredMixin, UpdateView):
    model = Vacation
    fields = '__all__'

class VacationDelete(LoginRequiredMixin, DeleteView):
    model = Vacation
    success_url = '/vacations/'

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

@login_required
def vacations(request):
    vacations = Vacation.objects.filter(user=request.user)
    return render(request, 'vacations/index.html', {'vacations': vacations})

@login_required
def vacation_detail(request, vacation_id):
    vacation = Vacation.objects.get(id=vacation_id)
    star_form = StarForm()
    return render(request, 'vacations/detail.html', {'vacation': vacation, 'star_form': star_form})

@login_required
def add_stars(request, vacation_id):
    form = StarForm(request.POST)
    if form.is_valid():
        new_star = form.save(commit=False)
        new_star.vacation_id = vacation_id
        new_star.save()
    return redirect('vacation-detail', vacation_id=vacation_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vacations')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('vacations/', views.vacations, name='vacations'),
    path('vacations/<int:vacation_id>/', views.vacation_detail, name='vacation-detail'),
    path('vacations/create/', views.VacationCreate.as_view(), name='vacation-create'),
    path('vacations/<int:pk>/update/', views.VacationUpdate.as_view(), name='vacation-update'),
    path('vacations/<int:pk>/delete/', views.VacationDelete.as_view(), name='vacation-delete'),
    path('vacations/<int:vacation_id>/add-stars/', views.add_stars, name='add-stars'),
    path('accounts/signup/', views.signup, name='signup'),
]


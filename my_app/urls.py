from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='restaurant-detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurant-create'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurant-update'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurant-delete'),
    path('restaurants/<int:restaurant_id>/add-stars/', views.add_stars, name='add-stars'),
]


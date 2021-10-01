from django.urls import path
from . import views

urlpatterns = [
    path('yelp/', views.yelp),
    path('businesses/', views.businesses)
]

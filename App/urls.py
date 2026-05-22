from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('twahda/', views.twahda),
    path('hadija/', views.hadija),
    path('summy/', views.summy),

]


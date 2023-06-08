from typing import List, Any

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name="ShopHome"),
path('about/', views.about, name="About"),
path('tracker/', views.tracker, name="Tracking Status"),
path('contact/', views.contact, name="Contact us"),
path('search/', views.search, name="Search"),
path("products/<int:myid>", views.productView, name="ProductView"),
path('checkout/', views.checkout, name="Checkout"),


]

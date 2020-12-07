from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home1, name='home'),
    path('customer/<int:id>/', views.customer, name='customers'),
    path('customer', views.customer, name='customers'),
    path('agents/<int:id>/', views.agent, name='agents'),
    path('agents/', views.agent, name='agents'),
    path('invoice/', views.invoice, name='invoice'),
    path('employee/', views.employee, name='employee'),
    path('medicine/', views.medicine, name='medicine'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join')
]
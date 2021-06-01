from django.contrib import admin
from django.urls import path
from .views import dashboard, rediret_index

name_app = 'app'

urlpatterns = [
    path('',  rediret_index),
    path('days=<int:days_range>/currencies=<str:currencies>', dashboard, name='home'),
]

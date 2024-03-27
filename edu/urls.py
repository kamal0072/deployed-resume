from . import views
from django.urls import path

urlpatterns = [
    path('skill/', views.skill, name="skill")
]

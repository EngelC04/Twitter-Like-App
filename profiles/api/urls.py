from django.contrib import admin
from django.urls import path, re_path
from .views import user_follow_view


"""
CLIENT
Base Endpoint /api/profile/
"""

urlpatterns = [
    path('<str:username>/follow/', user_follow_view),
]

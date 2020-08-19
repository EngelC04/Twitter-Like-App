from django.contrib import admin
from django.urls import path, re_path
from tweets.views import (home_view, tweet_detail_view, tweet_list_view, tweet_create_view)

urlpatterns = [
    path('home/', home_view),
    path('tweets/<int:tweet_id>', tweet_detail_view),
    path('create-tweet/', tweet_create_view),
    path('tweets/', tweet_list_view)
]
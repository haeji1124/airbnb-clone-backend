from django.urls import path
from .views import see_all_tweets

urlpatterns = [path("", see_all_tweets)]

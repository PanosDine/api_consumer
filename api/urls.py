from django.contrib import admin
from django.urls import path
from .views import LaunchesPage, launch_detail, search_launches, home

app_name="api"

urlpatterns = [
    path('', home, name="home"),
    path('launches', LaunchesPage.as_view(template_name='launches.html'), name='launches'),
    path('launches/<int:id>/', launch_detail, name="launch-detail"),
    path('search/', search_launches, name="search-launches"),
]
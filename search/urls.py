from django.urls import path 
from .views import search_posts

urlpatterns = [
    path('', search_posts, name='search')
]
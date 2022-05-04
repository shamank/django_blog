from django.urls import path
from .views import PostListView, home

urlpatterns = [
    path('', home),
    path('<slug:slugg>/', PostListView.as_view(), name='post_list')
]
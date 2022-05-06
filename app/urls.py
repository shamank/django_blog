from django.urls import path
from .views import FullPostListView, PostBlogView, PostListView

urlpatterns = [
    path('', FullPostListView.as_view(), name='home_page'),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostBlogView.as_view(), name='post_detail'),
]
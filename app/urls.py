from django.urls import path
from .views import FullPostListView, PostBlogView, PostListView, AboutUsView, CreateComment

urlpatterns = [
    path('', FullPostListView.as_view(), name='home_page'),
    path('about/', AboutUsView.as_view(), name='about_us'),
    path('post/<slug:slug>/', PostBlogView.as_view(), name='post_detail'),
    path('comment/<int:pk>', CreateComment.as_view(), name='create_comment'),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),


]
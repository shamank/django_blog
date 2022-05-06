from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class FullPostListView(ListView):
    model = Post 
    template_name = 'app/home_page.html'
    context_object_name = 'posts'


class PostListView(ListView):
    model = Post
    template_name = 'app/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).order_by('-created_at')


class PostBlogView(DetailView):
    model = Post
    

# def home(request):
#     return render(request, 'app/homepage.html')
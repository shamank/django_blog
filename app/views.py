from django.http import HttpResponseForbidden
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Post

# Create your views here.

import json 
import redis 

#edis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

class FullPostListView(ListView):
    model = Post 
    template_name = 'app/home_page.html'
    context_object_name = 'posts'
    paginate_by = 1


class PostListView(FullPostListView, ListView):
    # model = Post
    template_name = 'app/post_list.html'
    # context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).order_by('-created_at')


class AboutUsView(TemplateView):
    template_name = 'app/about.html'
    

class PostBlogView(DetailView):
    model = Post
    

# print all the hits
# for hit in search:
#     print(hit.title)

# def home(request):
#     return render(request, 'app/homepage.html')
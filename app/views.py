from django.http import HttpResponseForbidden
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post, Comment, View
from .forms import CommentForm

# Create your views here.

import json 
import redis 

#edis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

class FullPostListView(ListView):
    model = Post 
    template_name = 'app/home_page.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostListView(FullPostListView, ListView):
    # model = Post
    template_name = 'app/post_list.html'
    # context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).order_by('-created_at')


class AboutUsView(TemplateView):
    template_name = 'app/about.html'
    
class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm


    # def form_valid(self, form):
    #     # form.instance.post = self.request.
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk'))
        form.instance.created_by = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
class PostBlogView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated:
            View.objects.create(user=request.user, post=self.object)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


    
    

# print all the hits
# for hit in search:
#     print(hit.title)

# def home(request):
#     return render(request, 'app/homepage.html')
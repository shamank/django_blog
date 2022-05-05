from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post

    template_name = 'app/post_list.html'

    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug'))

    def get(self):
        if self.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()


def home(request):
    return render(request, 'app/homepage.html')
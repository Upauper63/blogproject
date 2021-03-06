from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class Index(ListView):
    template_name = 'index.html'
    model = Post
    paginate_by = 5
    queryset = Post.objects.order_by('-created_at')

class Detail(DetailView):
    template_name = 'detail.html'
    model = Post
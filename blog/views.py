from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body','preview']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:posts_list')

class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'



class PostUpdateView(UpdateView):
    model = Post
    fields = ["title","body"]
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:posts_list')
# Create your views here.


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')
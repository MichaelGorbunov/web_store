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
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-id")


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    def get_object(self):
        # Переопределение метода get_object для настройки логики выбора объекта
        obj = super().get_object()
        # Дополнительная логика (например,  изменения значений полей)
        # if not obj.is_active:
        #     raise Http404("Object not found")
        obj.views_count=obj.views_count+1
        obj.save()
        return obj






class PostUpdateView(UpdateView):
    model = Post
    fields = ["title","body","published","views_count"]
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:posts_list')
# Create your views here.


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')
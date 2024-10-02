from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post


class PostCreateView(CreateView):
    """создание поста"""
    model = Post
    fields = ['title', 'body', 'preview']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:posts_list')


class PostListView(ListView):
    """список постов"""
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # queryset = super().get_queryset().filter(published=True)
        # return queryset.order_by("-id")
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    """детальное описание поста"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    # def get_object(self):
    #     # Переопределение метода get_object
    #     obj = super().get_object()
    #     obj.views_count = obj.views_count + 1
    #     obj.save()
    #     return obj

    def get_object(self, queryset=None):
        # Переопределение метода get_object
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    """обновление поста"""
    model = Post
    fields = ["title", "body", "published", "preview", "views_count"]
    template_name = 'blog/post_form.html'

    # success_url = reverse_lazy('blog:posts_list')
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("blog:post_detail", kwargs={"pk": pk})


# Create your views here.


class PostDeleteView(DeleteView):
    """удаление поста"""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')

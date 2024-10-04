from django.urls import path,re_path
from .views import PostListView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView, PostList2View
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [

    path('', PostListView.as_view(), name='posts_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts_list2/', PostList2View.as_view(), name='posts_list2'),


]

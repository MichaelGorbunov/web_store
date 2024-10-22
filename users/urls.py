from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView,UserUpdateView
app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/catalog/'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('update/', UserUpdateView.as_view(template_name='users/register.html'), name='update'),
]
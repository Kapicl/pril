from django.urls import path
from .views import post_list, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", post_list, name="post_list"),
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

urlpatterns += [
    path("post/<int:post_id>/", post_detail, name="post_detail"),
]


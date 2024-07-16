from django.urls import path

from . import views
from .views import user_login

urlpatterns = [
    path("", views.UserIndexView.as_view(), name="index"),
    path("login/", user_login, name="login"),
]
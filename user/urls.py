from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserIndexView.as_view(), name="index")
]
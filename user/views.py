from django.shortcuts import render
from django.views.generic import TemplateView


class UserIndexView(TemplateView):
    template_name = "user/index.html"

from django.shortcuts import render
from django.views import generic

from .models import BaseItem


# Create your views here.

class IndexView(generic.ListView):
	template_name = "inventory/index.html"
	model = BaseItem

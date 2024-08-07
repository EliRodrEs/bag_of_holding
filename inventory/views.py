from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import generic

from .models import BaseItem


class IndexView(generic.ListView):
    template_name = "inventory/index.html"
    paginate_by = 20
    model = BaseItem
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search_term', '')
        if search_term:
            queryset = queryset.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term))
        return queryset

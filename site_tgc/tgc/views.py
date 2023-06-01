from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from tgc.models import Items
from tgc.utils import DataMixin


class SiteHome(DataMixin, ListView):
    model = Items
    template_name = 'tgc/index.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Items.objects.filter(quantity__gt=0)

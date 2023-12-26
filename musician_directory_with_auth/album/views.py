from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator   


# Create your views here.
@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form) :
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form) :
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('homepage')

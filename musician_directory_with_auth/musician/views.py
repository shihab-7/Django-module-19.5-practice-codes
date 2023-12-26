from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 


# Create your views here.
@method_decorator(login_required, name='dispatch')
class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request,'musician added successfully')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musician_lst'] = self.get_object()
        return context

    def form_valid(self, form):
        messages.success(self.request,'musician updated successfully')
        return super().form_valid(form)
    
# class MusicianDeleteView(DeleteView):
#     model = Musician
#     success_url = reverse_lazy('profile')

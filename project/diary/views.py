from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day
    paginate_by = 3


class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index') #/diary/


class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index') #/diary/


class DeleteView(generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')


class DetailView(generic.DetailView):
    model = Day
    success_url = reverse_lazy('diary:index')

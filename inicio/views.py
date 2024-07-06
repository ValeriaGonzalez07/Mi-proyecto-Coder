from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Bienvenido a mi Proyecto')

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MainModel
from .forms import MainModelForm # type: ignore
from django.urls import reverse_lazy

class MainModelListView(ListView):
    model = MainModel
    template_name = 'mainapp/mainmodel_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['object_list']:
            context['message'] = 'No hay objetos disponibles.'
        return context

class MainModelDetailView(DetailView):
    model = MainModel
    template_name = 'mainapp/mainmodel_detail.html'

class MainModelCreateView(CreateView):
    model = MainModel
    form_class = MainModelForm
    template_name = 'mainapp/mainmodel_form.html'
    success_url = reverse_lazy('mainmodel_list')

class MainModelUpdateView(UpdateView):
    model = MainModel
    form_class = MainModelForm
    template_name = 'mainapp/mainmodel_form.html'
    success_url = reverse_lazy('mainmodel_list')

class MainModelDeleteView(DeleteView):
    model = MainModel
    template_name = 'mainapp/mainmodel_confirm_delete.html'
    success_url = reverse_lazy('mainmodel_list')

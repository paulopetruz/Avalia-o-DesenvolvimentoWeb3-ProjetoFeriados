from logging import NullHandler
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from .forms import FeriadoForm
from API.models import FeriadoModel

# Create your views here.


def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'indexs.html', {'form': FeriadoForm()})

    if request.method == 'POST':
        form = FeriadoForm(request.POST)
        if form.is_valid():
            feriado = FeriadoModel(**form.cleaned_data)
            feriado.save()
    
            return render(request,'home.html',{'feriado': feriado})
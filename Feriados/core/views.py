from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from datetime import date
from API.models import FeriadoModel

# Create your views here.
def verify(request):
    hoje = date.today()
    qs = FeriadoModel.objects.all()
    if qs.filter(data=hoje):
        feriado = qs.filter(data=hoje)
    else:
        feriado = 'Não é feriado'
    return render(request, 'dias.html', {'feriado' : feriado})
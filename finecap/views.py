from django.shortcuts import render,get_object_or_404, redirect
from finecap.models import *
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from finecap.models import Reserva, Stand
from finecap.form import ReservaForm

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def cadastroReserva(request):
    if request.method == "POST":
        form=ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form=ReservaForm()
    else:
        form=ReservaForm()
    return render(request,'core/formReserva.html',{'form':form})

def listaReserva(request):
    listReserva = Reserva.objects.all()
    context= {

        "listReserva" : listReserva
    }

    return render(request, 'core/listaReserva.html', context)



def detalhe(request,id):
    reserva=get_object_or_404(Reserva, id=id)
    context={
        'reserva': reserva
    }
    return render(request, 'core/detalheReserva.html', context)


def editar(request, id):
    reserva=get_object_or_404(Reserva, id=id)
    if request.method == "POST":
        form=ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form=ReservaForm(instance=reserva)
        
    return render(request,'core/formReserva.html', {'form':form})

def remover(request,id):
    reserva = get_object_or_404(Reserva,id=id)
    reserva.delete()
    return redirect('lista')

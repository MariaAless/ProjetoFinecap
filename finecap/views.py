from django.shortcuts import render,get_object_or_404, redirect
from finecap.models import Reserva,Stand
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from finecap.form import ReservaForm
from django.urls import reverse_lazy
from django.contrib.messages import views
from users.permissions import GerentePermission


#---------------------VIEWS COM CBV------------------------------------

class index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context

class index2(TemplateView):
    template_name = "core/index2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context



class listReserva(ListView):
    template_name = 'core/listaReserva.html'
    model = Reserva
    context_object_name = 'reserva'
    paginate_by = 2



#criar
class Criar(views.SuccessMessageMixin,CreateView):

    form_class = ReservaForm
    template_name = 'core/formReserva.html'
    success_url = reverse_lazy('listar')
    success_message = "Reserva criada com sucesso!"


class Delete(GerentePermission,views.SuccessMessageMixin,DeleteView):
    model = Reserva
    template_name = 'core/confirm.html'
    success_url = reverse_lazy("listar")
    context_object_name= "reserva"
    success_message = "Reserva deletada com sucesso!"




class ReservaUpdateView(GerentePermission,views.SuccessMessageMixin,UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("listar")
  template_name = "core/formReserva.html"
  success_message = "Reserva atualizada com sucesso!"


class ReservaDetalhe(DetailView):
    model = Reserva
    template_name = "core/detalheReserva.html"





#----------------------------- VIEWS COM FUNÇÕES---------------------------------------

# def index(request):
#     return render(request, "core/index.html")
# def cadastroReserva(request):
#     if request.method == "POST":
#         form=ReservaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form=ReservaForm()
#     else:
#         form=ReservaForm()
#     return render(request,'core/formReserva.html',{'form':form})

# def listaReserva(request):
#     listReserva = Reserva.objects.all()
#     context= {

#         "listReserva" : listReserva
#     }

#     return render(request, 'core/listaReserva.html', context)



# def detalhe(request,id):
#     reserva=get_object_or_404(Reserva, id=id)
#     context={
#         'reserva': reserva
#     }
#     return render(request, 'core/detalheReserva.html', context)


# def editar(request, id):
#     reserva=get_object_or_404(Reserva, id=id)
#     if request.method == "POST":
#         form=ReservaForm(request.POST, instance=reserva)
#         if form.is_valid():
#             form.save()
#             return redirect('lista')
#     else:
#         form=ReservaForm(instance=reserva)
        
#     return render(request,'core/formReserva.html', {'form':form})

# def remover(request,id):
#     reserva = get_object_or_404(Reserva,id=id)
#     reserva.delete()
#     return redirect('lista')

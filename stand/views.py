from django.shortcuts import render,get_object_or_404, redirect
from finecap.models import Stand
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from stand.form import StandForm
from django.urls import reverse_lazy
from django.contrib.messages import views


#---------------------VIEWS COM CBV------------------------------------




class listStand(ListView):
   
    template_name ='stand/listarStand.html'
    model = Stand
    context_object_name = 'stand'
    paginate_by = 2



#criar
class CriarStand(views.SuccessMessageMixin,CreateView):

    form_class = StandForm
    template_name = 'stand/formStand.html'
    success_url = reverse_lazy('stand:listarStand')
    success_message = "Stand criado com sucesso!"


class Delete(views.SuccessMessageMixin,DeleteView):
    model = Stand
    template_name = 'stand/confirmStand.html'
    success_url = reverse_lazy("stand:listarStand")
    context_object_name= "stand"
    success_message = "Stand deletado com sucesso!"



class StandUpdateView(views.SuccessMessageMixin,UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand:listarStand")
  template_name = "stand/formStand.html"
  success_message = "Stand atualizado com sucesso!"


class StandDetalhe(DetailView):
    model = Stand
    template_name = "stand/detalheStand.html"

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from conteudo.forms import ContactForm
from conteudo.models import Secao, Servico, Contato, Portifolio


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        dados = super(Home, self).get_context_data(**kwargs)
        dados['secoes'] = Secao.objects.order_by('ordem')
        dados['servicos'] = Servico.objects.order_by('ordem')
        dados['contatos'] = Contato.objects.order_by('ordem')
        dados['form'] = ContactForm(self.request.GET or None)
        return dados


class PortifolioList(ListView):
    template_name = 'home.html'
    model = Portifolio
    
    

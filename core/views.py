from typing import overload
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario
from .forms import ContatoForm, ServicoModelForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class SolicitacaoView(FormView):
    template_name = 'solicitacao.html'
    form_class = ServicoModelForm
    success_url = reverse_lazy('solicitacao')

    def get_context_data(self, **kwargs):
        context = super(SolicitacaoView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        print(f"Entrou aqui!")
        form.save()
        messages.success(self.request, 'Sucesso ao realizar solicitação!')
        return super(SolicitacaoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        print("passou aqui")
        messages.error(self.request, 'Erro ao solicitar solicitação!')
        return super(SolicitacaoView, self).form_invalid(form, *args, **kwargs)


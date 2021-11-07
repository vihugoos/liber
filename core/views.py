from typing import overload
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, CustomUsuario
from .forms import ContatoForm, ServicoModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

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


class SolicitacaoView(LoginRequiredMixin, FormView):
    template_name = 'solicitacao.html'
    form_class = ServicoModelForm
    success_url = reverse_lazy('solicitacao')

    def get_context_data(self, **kwargs):
        context = super(SolicitacaoView, self).get_context_data(**kwargs)
        # context['usuarios'] = CustomUsuario.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Solicitação realizada com sucesso!')
        return super(SolicitacaoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao solicitar solicitação, tente novamente.')
        return super(SolicitacaoView, self).form_invalid(form, *args, **kwargs)



from django import forms
from django.core.mail.message import EmailMessage
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUsuario, SolicitacaoServico

class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'crm', 'cpf', 'rg', 'celular', 'plano')
        labels = {'username': 'E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user 
    

class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'crm', 'cpf', 'rg', 'celular', 'plano')


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f"Nome: {nome}\n\nE-mail: {email}\n\nAssunto: {assunto}\n\nMensagem: {mensagem}"

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@liber.com.br',
            to=['contato@liber.com.br'],
            headers={'Reply-to': email}
        )
        mail.send()


class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoServico
        fields = ['crm', 'nome', 'plano', 'tipo_de_servico', 'arquivo', 'mensagem', 'status', 'comprovante', 'observacao']


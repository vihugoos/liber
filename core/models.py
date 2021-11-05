from typing import DefaultDict
from django.db import models
from django.db.models.fields import CharField, TextField
from django.forms.widgets import Textarea
from stdimage.models import StdImageField 
from django import forms
import uuid

# Função para gerar nomes automáticos para uploads de arquivo 
def get_file_path(__instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


# Classe base que será utilizada em todas as tabelas do Banco de Dados 
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-home', 'Casa'),
        ('lni-car', 'Carro'),
        ('lni-bi-cycle', 'Moto'),
        ('lni-paperclip', 'Papel'),
        ('lni-agenda', 'Agenda'),
        ('lni-bolt-alt', 'Raio'),
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=13, choices=ICONE_CHOICES)
    nome_modal = models.CharField('Nome Modal', max_length=100, default="modal")

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, 
        variations={
            'thumb': {
                'width': 480, 
                'height': 480, 
                'crop': True
            }
        }
    )
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instragram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class SolicitacaoServico(Base):
    crm = models.IntegerField('Crm')
    nome = models.CharField('Nome', max_length=100)
    tipo_de_servico = CharField('Tipo de Serviço', max_length=100)
    arquivo = models.FileField('Arquivo', upload_to=get_file_path, blank=True)
    mensagem = models.TextField('Mensagem', max_length=450)

    def __str__(self):
        return self.nome


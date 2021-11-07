from django.contrib.auth.models import AbstractUser, BaseUserManager
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
    crm = models.CharField('Crm', max_length=13)
    nome = models.CharField('Nome', max_length=100)
    tipo_de_servico = CharField('Tipo de Serviço', max_length=100)
    arquivo = models.FileField('Arquivo', upload_to=get_file_path, blank=True)
    mensagem = models.TextField('Mensagem', max_length=450)

    def __str__(self):
        return self.nome


class UsuarioManager(BaseUserManager):
    use_in_migrations = True 

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório!')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser precisa ter is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser precisa ter is_superuser=True')
    
        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    crm = models.CharField('CRM', max_length=13)
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField('RG', max_length=14)
    celular = models.CharField('Celular', max_length=12)
    is_staff = models.BooleanField('Membro da equipe?', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UsuarioManager()

    def __str__(self):
        return self.email 



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import Cargo, Servico, Funcionario, SolicitacaoServico, CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('email', 'first_name', 'last_name', 'plano')
    fieldsets = (
        ('Credenciais de Login', {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'crm', 'cpf', 'rg', 'celular')}),
        ('Plano Contratado', {'fields': ('plano',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas ref. ao usuário', {'fields': ('last_login', 'date_joined')})
    )


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')


@admin.register(SolicitacaoServico)
class SolicitacaoServicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'plano', 'tipo_de_servico', 'data_criado', 'hora_criado', 'ativo')


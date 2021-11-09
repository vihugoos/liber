from django.urls import path
from .views import IndexView, SolicitacaoView, PerfilView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('solicitacao/', SolicitacaoView.as_view(), name='solicitacao'),
    path('perfil/', PerfilView.as_view(), name='perfil')
]


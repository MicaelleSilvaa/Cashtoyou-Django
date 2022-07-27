"""configurations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cashtoyou.views import home,sobre,cidades,perguntas,comofunciona,empresa,loginempresa, logincliente,conta,cliente,cadastroempresa,cadastrocliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('principais-cidades/', cidades),
    path('perguntas/', perguntas),
    path('comofunciona/', comofunciona),
    path('acesso/empresa/',empresa),
    path('acesso/login-empresa/',loginempresa),
    path('acesso/login-cliente/', logincliente),
    path('acesso/conta/',conta),
    path('acesso/cliente/',cliente),
    path('acesso/cadastro-empresa/',cadastroempresa),
    path('acesso/cadastro-cliente/',cadastrocliente),
    
]

handler404 = 'cashtoyou.views.page_not_found'
handler500 = 'cashtoyou.views.handler_server_error'
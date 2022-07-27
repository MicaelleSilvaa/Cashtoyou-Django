from django.contrib import admin
from cashtoyou.models import tb_cliente,tb_empresa


class cliente(admin.ModelAdmin):
    list_display= ('nome','email','bairro_endereco','cpf','pontuacao','data_cadastro')
    
class empresa(admin.ModelAdmin):
    list_display= ('nome','cnpj','bairro_endereco','setor','email','data_cadastro')
       
    
admin.site.register(tb_cliente, cliente)
admin.site.register(tb_empresa, empresa)

# Register your models here.


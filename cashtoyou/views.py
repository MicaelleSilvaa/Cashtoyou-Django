from contextlib import nullcontext
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from cashtoyou.models import tb_cliente,tb_empresa
from django.contrib.auth.hashers import make_password


# Create your views here.

def home(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def cidades(request):
    return render(request, 'principaisCidades.html')

def perguntas(request):
    return render(request, 'perguntasFrequentes.html')

def comofunciona(request):
    return render(request, 'comoFunciona.html')

def conta(request):
    return render(request, './acesso/criarConta.html')

def empresa(request):
    return render(request,'./acesso/empresa.html')

def cliente(request):
    return render(request, './acesso/cliente.html')

def loginempresa(request):
    return render(request,'./acesso/loginempresa.html')

def logincliente(request):
    return render(request, './acesso/logincliente.html')

def page_not_found(request,  exception):
    return render(request,'index.html')

def handler_server_error(request, *args, **argv):
     return render(request,'index.html', status = 500)


 
def cadastrocliente(request):
    data = {}    
    if request.method == 'POST':
        cpff = request.POST.get('cpf')       
        cliente = tb_cliente.objects.filter(cpf = cpff)         
        if not cliente.exists(): 
            data['msg'] = 'Cliente cadastrado com sucesso'
            data['class'] = 'alert alert-success'  
            criarcliente = tb_cliente()       
            criarcliente.nome = request.POST.get('nomecliente')
            criarcliente.cpf = request.POST.get('cpf')   
            criarcliente.fone = request.POST.get('tel1') 
            criarcliente.bairro_endereco = request.POST.get('endereco1')           
            criarcliente.email = request.POST.get('email1')
            criarcliente.endereco_bairro = request.POST.get('endereco1') 
            criarcliente.senha = make_password(request.POST.get('senha1'))
            criarcliente.save()            
            return render(request, './acesso/cliente.html', data)     
        else:
            data['msg'] = 'CPF já cadastrado'
            data['class'] = 'alert alert-danger'
            return render(request, './acesso/cliente.html', data) 
    else:
        data['msg'] = 'Cadastro não realizado'
        data['class'] = 'alert alert-danger'
        return render(request,'./acesso/cliente.html', data)



def cadastroempresa(request):
    data = {}    
    if request.method == 'POST':
        cnpj= request.POST.get('cnpj')       
        empresa = tb_empresa.objects.filter(cnpj = cnpj)       
        if not empresa.exists(): 
            data['msg'] = 'Empresa cadastrada com sucesso'
            data['class'] = 'alert alert-success'  
            criarempresa = tb_empresa()       
            criarempresa.nome = request.POST.get('nomeempresa')
            criarempresa.cnpj = request.POST.get('cnpj')   
            criarempresa.fone = request.POST.get('tel2')            
            criarempresa.email = request.POST.get('email2')  
            criarempresa.setor = request.POST.get('cargo')
            criarempresa.bairro_endereco = request.POST.get('endereco2')
            criarempresa.senha = make_password(request.POST.get('senha2'))
            criarempresa.save()            
            return render(request, './acesso/empresa.html', data)     
        else:
            data['msg'] = 'CNPJ já cadastrado'
            data['class'] = 'alert alert-danger'
            return render(request, './acesso/empresa.html', data) 
    else:
        data['msg'] = 'Cadastro não realizado'
        data['class'] = 'alert alert-danger'
        return render(request,'./acesso/empresa.html', data)




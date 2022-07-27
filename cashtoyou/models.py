from django.db import models 
# Create your models here.


class tb_categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=254)
    
    class Meta:           
        db_table = 'tb_categoria'    
        
class tb_empresa(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    cnpj = models.CharField(max_length=254, unique=True)
    nome = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    fone = models.CharField(max_length=254,blank=False)
    bairro_endereco = models.CharField(max_length=254, blank=False, verbose_name='Endereço')
    senha = models.CharField(max_length=254, null=False)
    setor = models.CharField(max_length=254)
   #cod_categoria = models.IntegerField    
    data_cadastro = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='Data de cadastro')  
    
    class Meta:           
        db_table = 'tb_empresa'    
        
class tb_grupo(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    area_bairro = models.CharField(max_length=254)
    cod_empresa = models.ForeignKey("tb_empresa", on_delete=models.CASCADE)
    
    class Meta:           
        db_table = 'tb_grupo'  

class tb_cliente(models.Model):
    codigo= models.BigAutoField(primary_key=True)
    cpf = models.CharField(max_length=254, unique=True)    
    nome = models.CharField(max_length=254)
    bairro_endereco = models.CharField(max_length=254, verbose_name='Endereço')    
    fone = models.CharField(max_length=254,null=False)
    email = models.CharField(max_length=254)
    senha = models.CharField(max_length=254, null=False)
    pontuacao = models.IntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True,editable=False, verbose_name='Data de cadastro' )  
    
    class Meta:           
        db_table = 'tb_cliente'  
     

class tb_cliente_empresa(models.Model): 
    codigo_clienteempresa = models.BigAutoField(primary_key=True)     
    cod_empresa = models.ForeignKey("tb_empresa", on_delete=models.CASCADE)    
    cod_cliente = models.ForeignKey("tb_cliente", on_delete= models.CASCADE)    
    data_cadastro = models.DateTimeField(auto_now_add=True,editable=False )  
    class Meta:   
        constraints = [
            models.UniqueConstraint(
                fields=['cod_empresa', 'cod_cliente'], name='unique_cod_empresa_cod_cliente_combination'
            )
        ]       
        db_table = 'tb_cliente_empresa'  
    
    
class historico_pontuacao(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    cod_cliente = models.BigIntegerField
    cod_empresa = models.BigIntegerField
    operacao = models.BigIntegerField
    pontuacao = models.BigIntegerField
    data_envio= models.DateTimeField(auto_now_add=True,editable=False) 
    class Meta:     
          
        db_table = 'historico_pontuacao'  

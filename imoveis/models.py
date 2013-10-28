# coding=UTF-8
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


class TipoOperacao(models.Model):
    descricao = models.CharField("descricao", max_length=200)
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name="Tipo de Operação"
        verbose_name_plural= "Tipos de Operação"
        ordering = ["descricao"]

class TipoImovel(models.Model):
    descricao = models.CharField("descricao", max_length=200)
    
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name="Tipo de Imóvel"
        verbose_name_plural="Tipos de Imóvel"
        ordering = ["descricao"]
        
class Bairro(models.Model):
    descricao = models.CharField("descrição", max_length=200)

    def __str__(self):
        return self.descricao
    
    class Meta:
        ordering = ["descricao"]


class Anuncio(models.Model):
    usuario = models.ForeignKey(User, blank=True)
    foto_capa = models.FileField(verbose_name="Foto / Vídeo", upload_to="fotos_de_capa",max_length=255, blank=True, null=True)
    tipoOperacao = models.ForeignKey(TipoOperacao,verbose_name="Operação")
    tipoImovel = models.ForeignKey(TipoImovel,verbose_name="Imóvel", help_text="Tipo de Imóvel")
    bairro = models.ForeignKey(Bairro, verbose_name="Bairro")
    descricao = models.TextField(max_length=500)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="área(m2)", blank=True, null=True, default=0)
    condominio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor do condomínio", blank=True, null=True, default=0)
    vagas_garagem = models.IntegerField(verbose_name="Garagem", blank=True, null=True, default=0, help_text="Número de vagas na garagem")
    salao_festas = models.BooleanField(verbose_name="Salão de Festas", default=False)
    area_lazer = models.BooleanField(verbose_name="Área de lazer", default=False)
    piscina = models.BooleanField(verbose_name="Piscina", default=False)
    academia = models.BooleanField(verbose_name="Academia", default=False)
    data_cadastro = models.DateField(verbose_name="Data de cadastro", default=date.today(), editable=False, auto_now_add=True )
    
    

    def __unicode__(self):
        return self.id + " - " + self.descricao[:50]
    
class Publicacao(models.Model):
    anuncio = models.ForeignKey(Anuncio, verbose_name="Anuncio")
    data_inicio = models.DateField(verbose_name="Data de início do anúncio", default=date.today())
    data_fim = models.DateField(verbose_name="Data de fim do anúncio")
    
    def __unicode__(self):
        return self.id + " - " + self.anuncio.descricao + "   " + self.data_inicio
    
    class Meta:
        verbose_name="Publicação"
        verbose_name_plural= "Publicações"
        ordering = ["data_inicio"]

class FotoAnuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, verbose_name="Anuncio")
    foto = models.FileField(verbose_name="foto", upload_to="fotos",max_length=255)    
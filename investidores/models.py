# coding=UTF-8
from django.db import models
from imoveis.models import Bairro, TipoImovel
from datetime import date
from django.contrib.auth.models import User
import decimal
from django.utils.formats import localize
from django.forms.widgets import Widget

INDIFERENTE_VARIACAO_METRO = decimal.Decimal('10')
VARIACAO_METRO_CHOICES = (
      (INDIFERENTE_VARIACAO_METRO, 'Indiferente'),
      (decimal.Decimal('0.75'), 'Até 25% abaixo do valor do preço médio do m2'),                  
      (decimal.Decimal('0.80'), 'Até 20% abaixo do valor do preço médio do m2'),
      (decimal.Decimal('0.85'), 'Até 15% abaixo do valor do preço médio do m2'),
      (decimal.Decimal('0.90'), 'Até 10% abaixo do valor do preço médio do m2'),
      (decimal.Decimal('0.95'), 'Até 05% abaixo  do valor do preço médio do m2'),
      (decimal.Decimal('1.05'), 'Até 05% acima do valor do preço médio do m2'),
      (decimal.Decimal('1.10'), 'Até 10% acima do valor do preço médio do m2'),
      (decimal.Decimal('1.15'), 'Até 15% acima do valor do preço médio do m2'),
      (decimal.Decimal('1.20'), 'Até 20% acima do valor do preço médio do m2'),
      (decimal.Decimal('1.25'), 'Até 25% acima do valor do preço médio do m2'),
)

INDIFERENTE_CONDOMINIO = decimal.Decimal('99999.99')
CONDOMINIO_CHOICES = (
      (INDIFERENTE_CONDOMINIO,       'Indiferente'     ),
      (decimal.Decimal('0.00'),      'Sem condomínio'  ),
      (decimal.Decimal('100.00'),    'R$ 100,00'       ),                  
      (decimal.Decimal('200.00'),    'R$ 200,00'       ),
      (decimal.Decimal('300.00'),    'R$ 300,00'       ),
      (decimal.Decimal('400.00'),    'R$ 400,00'       ),                  
      (decimal.Decimal('500.00'),    'R$ 500,00'       ),
      (decimal.Decimal('600.00'),    'R$ 600,00'       ),
      (decimal.Decimal('700.00'),    'R$ 700,00'       ),
      (decimal.Decimal('800.00'),    'R$ 800,00'       ),                  
      (decimal.Decimal('900.00'),    'R$ 900,00'       ),
      (decimal.Decimal('1000.00'), 'R$ 1.000,00'       ),
)

INIFERENTE_VALOR_MAXIMO_IMOVEL = decimal.Decimal('999999999999.99')
VALOR_MAXIMO_IMOVEL_CHOICES= (
      (INIFERENTE_VALOR_MAXIMO_IMOVEL, 'Indiferente'                            ),
      (decimal.Decimal ( '50000.00'),  'até R$    50.000,00 (cinquenta mil)'    ),
      (decimal.Decimal ('100000.00'),  'até R$   100.000,00 (cem mil)'          ),
      (decimal.Decimal ('200000.00'),  'até R$   200.000,00 (duzentos mil)'     ),
      (decimal.Decimal ('300000.00'),  'até R$   300.000,00 (trezentos mil)'    ),
      (decimal.Decimal ('400000.00'),  'até R$   400.000,00 (quatrocentos mil)' ),
      (decimal.Decimal ('500000.00'),  'até R$   500.000,00 (quinentos mil)'    ),
      (decimal.Decimal ('600000.00'),  'até R$   600.000,00 (seiscentos mil)'   ),
      (decimal.Decimal ('700000.00'),  'até R$   700.000,00 (setecentos mil)'   ),
      (decimal.Decimal ('800000.00'),  'até R$   800.000,00 (oitocentos mil)'   ),
      (decimal.Decimal ('900000.00'),  'até R$   900.000,00 (novecentos mil)'   ),
      (decimal.Decimal('1000000.00'),  'até R$ 1.000.000,00 (um milhão)'        ),                        
                              
)

INIFERENTE_VALOR_MAXIMO_M2 = decimal.Decimal('999999999999.99')
VALOR_MAXIMO_M2_CHOICES= (
      (INIFERENTE_VALOR_MAXIMO_M2,   'Indiferente'),
      (decimal.Decimal ('1000.00'),  'até R$ 1.000,00'),
      (decimal.Decimal ('1500.00'),  'até R$ 1.500,00'),
      (decimal.Decimal ('2000.00'),  'até R$ 2.000,00'),
      (decimal.Decimal ('2500.00'),  'até R$ 2.500,00'),
      (decimal.Decimal ('3000.00'),  'até R$ 3.000,00'),
      (decimal.Decimal ('3500.00'),  'até R$ 3.500,00'),
      (decimal.Decimal ('4000.00'),  'até R$ 4.000,00'),
      (decimal.Decimal ('4500.00'),  'até R$ 4.500,00'),
      (decimal.Decimal ('5000.00'),  'até R$ 5.000,00'),
      (decimal.Decimal ('5500.00'),  'até R$ 5.500,00'),
      (decimal.Decimal ('6000.00'),  'até R$ 6.000,00'),
)

IDADE_MAXIMA_INDIFERENTE = 999
IDADE_MAXIMA_CHOICES = (
        (IDADE_MAXIMA_INDIFERENTE, 'Indiferente'), 
        (0,  'Novo ou Em Construção'),
        (3,  'até  3 anos'),
        (5,  'até  5 anos'),
        (10, 'até 10 anos'),
        (15, 'até 15 anos'),
        (20, 'até 20 anos'),
)

#class VariacaoMetro(models.Model):
#    valor = models.DecimalField(verbose_name="Variação máxima do m2", max_digits=5, decimal_places=2)
#    descricao = models.CharField(max_length=100)   

class Desejo(models.Model):
    usuario = models.ForeignKey(User, blank=True)
    descricao = models.CharField(max_length=100, blank=True, null=True, help_text="Digite um texto para identificar o seu desejo")
    tiposImoveis = models.ManyToManyField(TipoImovel)
    bairros = models.ManyToManyField(Bairro)
    qtd_quartos_min = models.IntegerField(verbose_name="Quantidade mínima de quartos", default=0)
    qtd_suites_min = models.IntegerField(verbose_name="Quantidade mínima de suites", default=0)
    area_min = models.IntegerField(verbose_name="Área mínima em m2", default=0)
    area_max = models.IntegerField(verbose_name="Área máxima em m2", default=99999)
    condominio_max = models.DecimalField(verbose_name="Valor máximo de condomínio", max_digits=16, decimal_places=2, 
                                        choices = CONDOMINIO_CHOICES,
                                        default = INDIFERENTE_CONDOMINIO
                                    )
    idade_max = models.IntegerField(verbose_name="Idade máxima do imóvel",
                                        choices = IDADE_MAXIMA_CHOICES, 
                                        default = IDADE_MAXIMA_INDIFERENTE,
                                    )
    valor_imovel_max = models.DecimalField(verbose_name="Valor máximo do imóvel",max_digits=16, decimal_places=2,
                                        choices = VALOR_MAXIMO_IMOVEL_CHOICES, 
                                        default = INIFERENTE_VALOR_MAXIMO_IMOVEL,   
                                    )
    valor_metro_max = models.DecimalField(verbose_name="Valor máximo do m2",max_digits=16, decimal_places=2,
                                        choices = VALOR_MAXIMO_M2_CHOICES, 
                                        default = INIFERENTE_VALOR_MAXIMO_M2, 
                                    )
    variacao_metro = models.DecimalField(verbose_name="Variação máxima do m2", max_digits=16, decimal_places=2,
                                        choices = VARIACAO_METRO_CHOICES,
                                        default = INDIFERENTE_VARIACAO_METRO
                                    )
    
    #deve_ter_piscina = models.BooleanField(verbose_name="Deve ter piscina", default=False)
    #deve_ter_academia
    #deve ter area_de_lazer
    data_cadastro = models.DateField(verbose_name="Data de cadastro", auto_now_add=True)
    data_pagamento = models.DateField(verbose_name="Data do pagamento", blank=True, null=True)
    data_publicacao = models.DateField(verbose_name="Data de publicação",blank=True, null=True)
    expirado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name="Desejo"
        verbose_name_plural= "Desejos"
        ordering = ["data_publicacao"]
    
    @property    
    def TiposImoveis(self):
        tiposImoveis = self.tiposImoveis.all()
        descricoes_tiposImoveis = ', '.join(tipoImovel.descricao for tipoImovel in tiposImoveis )
        return descricoes_tiposImoveis
    
    @property
    def Bairros(self):
        bairros = self.bairros.all()
        descricoes_bairros = ', '.join(bairro.descricao for bairro in bairros)
        return descricoes_bairros
    
    def __str__(self):
        
        if self.descricao:
            return self.descricao
        return " | ".join((self.usuario.username, self.usuario.email, ('Tipos: ' + self.TiposImoveis), 
                           ('Bairros: ' + self.Bairros), ('Valor máx imóvel: ' + str(self.valor_imovel_max)), 
                           ('Valor max var. m2: ' + str(self.variacao_metro))
                           ))


class PrecoMedioBairro(models.Model):
    bairro = models.OneToOneField(Bairro)
    preco_medio = models.DecimalField(verbose_name="preço médio do m2", max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name="Preço médio do m2 por bairro"
        ordering = ["bairro"]
        
    def __str__(self):
        return self.bairro.__str__() + " - R$ " +  str(self.preco_medio)
    
    

from imoveis.models import Anuncio, TipoImovel, TipoOperacao, Bairro, Publicacao, FotoAnuncio
from django.contrib import admin


admin.site.register(TipoOperacao)
admin.site.register(TipoImovel)
admin.site.register(Anuncio)
admin.site.register(Bairro)
admin.site.register(Publicacao)
admin.site.register(FotoAnuncio)
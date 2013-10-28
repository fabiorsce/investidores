from investidores.models import Desejo, PrecoMedioBairro
from django.contrib import admin
from django.contrib.admin.sites import AdminSite

class MyAdminSite(AdminSite):
    pass
    #or overwrite some methods for different functionality

admin.site.register(Desejo)
admin.site.register(PrecoMedioBairro)



class DesejoMyadmin(admin.ModelAdmin):
    exclude = ('usuario', 'data_pagamento','data_publicacao', 'expirado',)
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(DesejoMyadmin, self).queryset(request)
        return qs.filter(usuario=request.user)
    
myadmin = MyAdminSite(name='myadmin')
myadmin.register(Desejo, DesejoMyadmin)

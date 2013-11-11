from investidores.models import Desejo, PrecoMedioBairro
from django.contrib import admin
from django.contrib.admin.sites import AdminSite


class DesejoAdmin(admin.ModelAdmin):
    exclude = ('usuario', 'data_pagamento','data_publicacao', 'expirado',)
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(DesejoAdmin, self).queryset(request)
        return qs.filter(usuario=request.user)


admin.site.register(Desejo,DesejoAdmin)
admin.site.register(PrecoMedioBairro)



    

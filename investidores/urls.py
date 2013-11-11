from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'investidores.views.user.home', name='home'),
    url(r'^investidores/add/', 'investidores.views.desejo.add'),

    url(r'^registrar/$', 'investidores.views.user.registrar', name='pagina_de_registro'), # pagina de cadastro
    url(r'^login/$', 'investidores.views.user.logar', name='pagina_de_login'), # pagina de login    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^myadmin/', include(myadmin.urls)),
)

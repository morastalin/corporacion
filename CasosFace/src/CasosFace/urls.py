from django.conf.urls import patterns, include, url
from CasosFace.views import current_datetime, hours_ahead, nuevo_author, listBook

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^time/$' , current_datetime),
    #('^cat_1/$' , cat_1),
    #('^cat_2/$' , cat_2),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    (r'^', include('Seguridades.urls')),
    (r'^nuevo_author/$',nuevo_author),
    (r'^list_author/$',listBook),
    
    #('^hello/$', hello),
    # Examples:
    # url(r'^$', 'CasosFace.views.home', name='home'),
    # url(r'^CasosFace/', include('CasosFace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

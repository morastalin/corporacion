from django.conf.urls import patterns, include, url
from Seguridades.views import main_page, sign_post

urlpatterns = patterns('',
    (r'^sign/$', sign_post),
    (r'^$', main_page),
)
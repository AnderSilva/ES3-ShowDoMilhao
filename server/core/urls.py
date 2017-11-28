# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy

urlpatterns = patterns('',
       url(r'^api/v1/pergunta'  , include('pergunta.urls')),
       url(r'^api/v1/user'      , include('user.urls')),
       url(r'^api/v1/jogo'      , include('jogo.urls')),
       url(r'^api/v1/comprar'   , include('item.urls')),
       url(r'^api/v1/$|^'       , include('rest_framework_docs.urls')),
       #url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
)

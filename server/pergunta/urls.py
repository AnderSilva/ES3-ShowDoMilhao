# -*- coding: utf-8 -*-
from django.conf.urls import url

from pergunta.views import PerguntaCreateView, PerguntaDetailView, PerguntaListView, PerguntaRandomView
from pergunta.views import PerguntaAlternativaView

urlpatterns = [
    url(r'^/random' 		, PerguntaRandomView.as_view()	, name='pergunta_random'),
    url(r'^/create'			, PerguntaCreateView.as_view()	, name='pergunta_create'),
    url(r'^/(?P<pk>[0-9]+)$', PerguntaDetailView.as_view()	, name='pergunta_detail'),
    url(r'^/(?P<id_pergunta>[0-9]+)/alternativa/(?P<id_alternativa>[0-9]+)$'
    	                    , PerguntaAlternativaView.as_view()	, name='pergunta_alternativa'),
    url(r'^/list$'			, PerguntaListView.as_view()	, name='pergunta_list'),  
]

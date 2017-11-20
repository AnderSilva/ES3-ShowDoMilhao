# -*- coding: utf-8 -*-
from django.conf.urls import url

from pergunta.views import PerguntaCreateView, PerguntaDetailView, PerguntaListView, PerguntaRandomView
from pergunta.views import PerguntaAlternativaView

urlpatterns = [
    url(r'^/random' 		, PerguntaRandomView.as_view()	, name='pergunta_random'),
    url(r'^/create'			, PerguntaCreateView.as_view()	, name='pergunta_create'),
    url(r'^/list'			, PerguntaListView.as_view()	, name='pergunta_list'),
    url(r'^/(?P<pk>[0-9]+)$', PerguntaDetailView.as_view()	, name='pergunta_detail'),
    url(r'^/(?P<id_pergunta>[0-9]+)/alternativa/(?P<id_alternativa>[0-9]+)$', PerguntaAlternativaView.as_view()	, name='pergunta_alternativa'),
    # url(r'^alternativa/$'			, AlternativaDetailView.as_view()	, name='alternativa_detail'),

   # url(r'^login/$'					, UserCreateView.as_view()		, name='user_create'),
	#url(r'^pergunta/(?P<pk>[0-9]+)$', PerguntaDetailView.as_view()	, name='detail'),

]



# from django.conf.urls import patterns, include, url
# from rest_framework import routers

# router = routers.DefaultRouter()

# urlpatterns = patterns('api.views',
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# )

from django.conf.urls import url
from item.views import ItensListView,ItensComprarView,ItensComprarPontosView

urlpatterns = [
	url(r'^/list$'   , ItensListView.as_view()),
    url(r'^/item/(?P<item_id>[0-9]+)/(?P<qtde>[0-9]+)$'   
    				 , ItensComprarView.as_view()),    
    url(r'^/pontos/(?P<qtde_pontos>[0-9]+)$'
    				, ItensComprarPontosView.as_view()),    
    
]

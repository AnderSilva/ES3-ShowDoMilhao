from django.conf.urls import url
from jogo.views import JogoRecuperarCreateView ,JogoListView,JogoDeletarView

urlpatterns = [
    url(r'^/get$', JogoRecuperarCreateView.as_view()),
    url(r'^/list$', JogoListView.as_view()),
    url(r'^/del$', JogoDeletarView.as_view()),
]

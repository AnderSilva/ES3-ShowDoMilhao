from django.conf.urls import url
from jogo.views import JogoRecuperarCreateView ,JogoListView, JogoCreateView

urlpatterns = [
    url(r'^/get$', JogoRecuperarCreateView.as_view()),
    url(r'^/list$', JogoListView.as_view()),
    url(r'^/create$', JogoCreateView.as_view()),
]

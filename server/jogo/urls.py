from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from jogo.views import JogoRecuperarCreateView

urlpatterns = [
    url(r'^/get$', JogoRecuperarCreateView.as_view()),
]

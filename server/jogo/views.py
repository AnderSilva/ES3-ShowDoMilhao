from jogo.models import Jogo
from jogo.serializers import JogoSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.core.exceptions import ObjectDoesNotExist
import random as rand

'''
    View abaixo recupera algum jogo em andamento do ou cria um novo jogo
'''
class JogoRecuperarCreateView(ListAPIView):
    permission_classes = (IsAuthenticated, )# permission_classes= (AllowAny,)    
    authentication_classes = (JSONWebTokenAuthentication,)
    
    queryset = Jogo.objects.filter(is_active=True)
    serializer_class = JogoSerializer

    # def get(self, request):
    #     jogo = Jogo.objects.filter(id_usuario=request.user.id,is_active=True)
    #     return JogoSerializer(jogo).data

    # def get(self, request):
    #     data = {
    #         # 'id': request.user.id,
    #         'username': request.user.username,
    #         'token': str(request.auth)
    #     }        
    #     return Response(data)

    # def get(self,request):
    #     serializer = self.serializer_class(data=request.data)
    #     print dir(request)
    #     print '************************************'
    #     print request.user.id
    #     print '************************************'
    #     print request.user.username
    #     print '************************************'
    #     print request.auth
    #     print '************************************'
    #     # try:
    #     #     jogo = Jogo.objects.filter(id_usuario=id_pergunta,id_alternativa=id_alternativa).get().resposta
    #     # except ObjectDoesNotExist: #Usuario nao tem jogo ativo
    #     #     return Response(data={-1:'Vini, para de malandragem!'},status=status.HTTP_200_OK)
    #     #
    #     # if respostaBD=='1':
    #     #     #TODO salvar pontuacao no halldafama
    #     #     return Response(data={1:'Resposta Correta!'},status=status.HTTP_200_OK)
    #     # else:
    #     #     #TODO remover pontuacao devido ao erro
    #     return Response(data={0:'Teste'},status=status.HTTP_200_OK)

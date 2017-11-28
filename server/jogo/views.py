from jogo.models import Jogo
from user.models import Usuario
from item.models import UsuarioItem
from jogo.serializers import JogoSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from user.helper import IsAdmin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.core.exceptions import ObjectDoesNotExist
import random as rand


class JogoRecuperarCreateView(ListAPIView):
    '''
        Cria um novo jogo / Recupera algum jogo em andamento
    '''
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,)
    
    queryset = Jogo.objects.filter(is_active=True)
    serializer_class = JogoSerializer    

    def get(self, request):

        try:            
            jogo = Jogo.objects.get(usuario_id=request.user.id,is_active=True)
        except ObjectDoesNotExist:
            jogo = Jogo.objects.create(usuario_id=request.user.id)

        return Response(self.serializer_class(jogo).data, status=status.HTTP_200_OK)

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

class JogoDeletarView(UpdateAPIView):
    '''
        Desativar permanentemente um jogo em andamento
    '''
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,)
    
    queryset = Jogo.objects.filter(is_active=True)
    serializer_class = JogoSerializer    

    def put(self, request):

        try:            
            jogo = Jogo.objects.get(usuario_id=request.user.id,is_active=True)
            jogo.is_active = False
            jogo.save()
        except ObjectDoesNotExist:
            return Response(data={'Erro' : 'Jogo Inexistente'}, status=status.HTTP_404_NOT_FOUND)
                            
        return Response(data={'Jogo inativado:':JogoSerializer(jogo).data}, status=status.HTTP_200_OK)

class JogoListView(ListAPIView):
    '''
        Lista todos os jogos ativos (AdminOnly)
    '''
    permission_classes= (IsAdmin,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

    
class JogoUsarItemView(UpdateAPIView):
    '''
        Consumo de itens durante o jogo
    '''
    permission_classes= (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Usuario.objects.all()
    serializer_class = UserStatusSerializer

    def put(self, request, item_id):
        item = Item.objects.get(pk=item_id)
        try:        
            usuarioitem = UsuarioItem.objects.get(usuario_id=request.user.id, item=item)
        except ObjectDoesNotExist:
            return Response(data={'Erro' : 'Item Inexistente para consumo'}, status=status.HTTP_404_NOT_FOUND)

        usuarioitem.qtde -= 1        
        usuarioitem.save()

        if usuarioitem.qtde == 0:
            usuarioitem.delete()

        user = Usuario.objects.get(pk=request.user.id)
        return Response(UserStatusSerializer(user).data,status=status.HTTP_200_OK)
from item.models import Item, UsuarioItem
from user.models import Usuario
from item.serializers import ItemSerializer,UsuarioItemSerializer
from user.serializers import UserStatusSerializer

from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from user.helper import IsAdmin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.core.exceptions import ObjectDoesNotExist


# class JogoRecuperarCreateView(ListAPIView):
#     '''
#         Cria um novo jogo / Recupera algum jogo em andamento
#     '''
#     permission_classes = (IsAuthenticated, )
#     authentication_classes = (JSONWebTokenAuthentication,)
    
#     queryset = Jogo.objects.filter(is_active=True)
#     serializer_class = JogoSerializer    

#     def get(self, request):

#         try:            
#             jogo = Jogo.objects.get(usuario_id=request.user.id,is_active=True)
#         except ObjectDoesNotExist:
#             jogo = Jogo.objects.create(usuario_id=request.user.id)

#         return Response(self.serializer_class(jogo).data, status=status.HTTP_200_OK)


class ItensListView(ListAPIView):
    '''
        Lista todos os produtos ativos (All)
    '''
    permission_classes= (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItensComprarView(UpdateAPIView):
    '''
        Comprar produtos
    '''
    usuario = serializers.IntegerField(required=True) #,write_only=True)
    item    = serializers.IntegerField(required=True) #,write_only=True)
    qtde    = serializers.IntegerField(required=True) #,write_only=True)

    permission_classes= (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Item.objects.all()
    serializer_class = UsuarioItemSerializer

    def put(self, request, item_id, qtde):
        item = Item.objects.get(pk=item_id)
        try:        
            usuarioitem = UsuarioItem.objects.get(usuario_id=request.user.id, item=item)
        except ObjectDoesNotExist:
            usuarioitem = UsuarioItem.objects.create(usuario_id=request.user.id, item=item)

        usuarioitem.qtde += int(qtde)
        usuarioitem.save()                  

        return Response(UsuarioItemSerializer(usuarioitem).data,status=status.HTTP_200_OK)

class ItensComprarPontosView(UpdateAPIView):
    '''
        Lista todos os produtos ativos (All)
    '''
    permission_classes= (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Usuario.objects.all()
    serializer_class = UserStatusSerializer

    def put(self, request, qtde_pontos):
        user = Usuario.objects.get(pk=request.user.id)
        user.pontos += int(qtde_pontos)
        
        user.save()

        return Response(UserStatusSerializer(user).data,status=status.HTTP_200_OK)
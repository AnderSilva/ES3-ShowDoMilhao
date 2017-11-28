from jogo.models import Jogo, JogoPerguntas
from pergunta.models import Alternativa
from user.models import Usuario
from item.models import UsuarioItem, Item
from jogo.serializers import JogoSerializer
from user.serializers import UserStatusSerializer
from pergunta.serializers import AlternativaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from user.helper import IsAdmin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.core.exceptions import ObjectDoesNotExist
import random


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
        1 -> Carta
        2 -> Pulo
        3 -> Voto Popular
    '''
    permission_classes= (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Usuario.objects.all()
    serializer_class = UserStatusSerializer

    def put(self, request, item_id, id_pergunta):
        try:
            id_JogoBD = Jogo.objects.filter(usuario_id=request.user.id,is_active=True).last().id
            id_perguntaBD = JogoPerguntas.objects.filter(jogo_id=id_JogoBD).last().id_pergunta.id_pergunta
        except ObjectDoesNotExist:
            return Response(data={'Erro' : 'JogoID ou PerguntaID Invalidos.'}, status=status.HTTP_404_NOT_FOUND)

        if int(id_perguntaBD)!=int(id_pergunta):
            return Response(data={'Erro' : 'PerguntaID nao corresponde a pergunta atual.'}, status=status.HTTP_404_NOT_FOUND)

        item = Item.objects.get(pk=item_id)
        try:        
            usuarioitem = UsuarioItem.objects.get(usuario_id=request.user.id, item=item)
        except ObjectDoesNotExist:
            return Response(data={'Erro' : 'Item Inexistente para consumo'}, status=status.HTTP_404_NOT_FOUND)

        usuarioitem.qtde -= 1
        usuarioitem.save()

        if usuarioitem.qtde == 0:
            usuarioitem.delete()            

        if item.nome == 'carta':
            print 'carta'
            cartas = random.randrange(0,3)
            alternativas = Alternativa.objects.filter(id_pergunta=id_pergunta)
            alt_res = list(alternativas.values_list('id_alternativa','resposta'))
        
            for i in range(0,cartas):
                if int(alt_res[i][1])==0:
                    alt_res.pop(i)

            alter_fil = [alt_res[i][0] for i in range(0,len(alt_res))]
            alternativas = alternativas.filter(id_alternativa__in=alter_fil)
            return Response(AlternativaSerializer(alternativas,many=True).data,status=status.HTTP_200_OK)


        elif item.nome == 'voto popular':
            print 'voto popular'

            percErro = [random.randrange(10,30) for i in range(0,3)]
            percCerto= 100-sum(percErro)
            
            alternativas = Alternativa.objects.extra(select={'percentual': 0}).filter(id_pergunta=id_pergunta)
            alt_res = list(alternativas.values_list('percentual','id_alternativa','resposta','alternativa'))
            alt_res2 = [list(alt_res[i]) for i in range(0,len(alt_res))]
            
            x  = 0
            for i in range(0,len(alternativas)):
                if int(alt_res[i][2])==0:
                    alt_res2[i][0] = percErro[x]
                    x += 1
                else:
                    alt_res2[i][0] = percCerto
                    pass
                
            pass

            data = [{'id_pergunta':id_pergunta, 'id_alternativa': i[1],'alternativa':i[3], 'resposta' : i[2], 'percentual': i[0]} for i in alt_res2]
            return Response(data, status=status.HTTP_200_OK)

        #elif item.nome == 'pulo': #nao faz nada, agora pode baixar outra questao

        return Response(data={'Mensagem':'Pulo efetuado, pode chamar a proxima pergunta!'},status=status.HTTP_200_OK)
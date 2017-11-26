from pergunta.models import Pergunta , Alternativa
from jogo.models import Jogo, PontosTimer
from user.models import Usuario
from pergunta.serializers import PerguntaSerializer, AlternativaSerializer,AlternativaRespostaSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from user.helper import IsAdmin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.core.exceptions import ObjectDoesNotExist
import random as rand

class PerguntaListView(ListCreateAPIView):
    """
    Lista as perguntas do Sistema (AdminOnly)
    """
    permission_classes = (IsAdmin, )
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaCreateView(ListAPIView):
    """
    Criacao de perguntas (AdminOnly)
    """
    permission_classes = (IsAdmin, )
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer



class PerguntaAlternativaView(RetrieveAPIView):
    """
    Valida a resposta do usuario (Qualquer user autenticado em um jogo em andamento)
    """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,)

    queryset = Alternativa.objects.all()
    serializer_class = AlternativaRespostaSerializer
    
    def ObtemPontuacao(self, tempo=None):        
        if tempo is None:
            return 5
        
        pontosTabela = PontosTimer.objects.order_by('ate_segundos')
        segundos_min = pontosTabela.first()
        segundos_max = pontosTabela.last()
        
        if   timer >= segundos_max.ate_segundos:
            pontos = segundos_max.pontos
        elif timer <= segundos_min.ate_segundos:
            pontos = segundos_min.pontos
        else:
            pontos = pontosTabela.filter(ate_segundos__gte=timer)[0].pontos

        return pontos



    def get(self,request, id_alternativa, id_pergunta, tempo=None):
        try:
            respostaBD = Alternativa.objects.filter(id_pergunta=id_pergunta,id_alternativa=id_alternativa).get().resposta
        except ObjectDoesNotExist:
            return Response(data={-1:'Vini, para de malandragem!'},status=status.HTTP_400_BAD_REQUEST)

        user = Usuario.objects.get(id=request.user.id)
        if respostaBD=='1':
            #TODO salvar no log        
            jogo = Jogo.objects.get(usuario_id=11,is_active=True)
            jogo.acertos = jogo.acertos+1
            jogo.save()

            pontos = self.ObtemPontuacao(tempo)            
            user.pontos = user.pontos + pontos
            user.save()

            return Response(data={1:'Resposta Correta!'},status=status.HTTP_200_OK)
        else:
            #TODO salvar no log
            pontos = -10            
            user.pontos = user.pontos + pontos            
            user.save()

            return Response(data={0:'Resposta Errada!'},status=status.HTTP_200_OK) #HTTP_406_NOT_ACCEPTABLE


class PerguntaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaRandomView(ListAPIView):
    # permission_classes= (IsAuthenticated,)
    serializer_class = PerguntaSerializer

    def get_queryset(self):
        pk = rand.randint(1,300)
        print request
        #implementar busca das perguntas ja processadas
        return Pergunta.objects.filter(pk=pk)
    pass


# class AlternativaCreateView(ListCreateAPIView):
#     queryset = Alternativa.objects.all()
#     serializer_class = AlternativaSerializer

class AlternativaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer

# class AlternativaDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Alternativa.objects.all()
#     serializer_class = AlternativaSerializer

#

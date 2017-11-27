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
import random


class PerguntaListView(ListCreateAPIView): #/list
    """
    Lista as perguntas do Sistema (AdminOnly)
    """
    permission_classes = (IsAdmin, )
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaCreateView(ListAPIView):  #/create
    """
    Criacao de perguntas (AdminOnly)
    """
    permission_classes = (IsAdmin, )
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaAlternativaView(RetrieveAPIView): #/<pk>/alternativa/<pk>
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
            jogo = Jogo.objects.get(usuario_id=user.id,is_active=True)
            jogo.acertos = jogo.acertos+1
            jogo.save()

            pontos = self.ObtemPontuacao(tempo)            
            user.pontos = user.pontos + pontos
            user.save()

            return Response(data={1:'Resposta Correta!'},status=status.HTTP_200_OK)
        else:            
            pontos = -10            
            user.pontos = user.pontos + pontos            
            user.save()

            return Response(data={0:'Resposta Errada!'},status=status.HTTP_200_OK) #HTTP_406_NOT_ACCEPTABLE

class PerguntaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaRandomView(ListAPIView):  #/random
    permission_classes= (IsAuthenticated,)
    serializer_class = PerguntaSerializer

    def get_queryset(self):
        #perguntas_usadas = buscar tabela log
        #perguntas_possiveis = Pergunta.objects.values_list('id_pergunta',flat=True).exclude(id_pergunta__in=perguntas_usadas)
        #pk = random.choices(lista_perguntas)
        
        pk = random.randint(1,300)        
        obtem_Pergunta = True
        while obtem_Pergunta:            
            try:
                pergunta = Pergunta.objects.filter(pk=pk)
                obtem_Pergunta = False
            except ObjectDoesNotExist:
                obtem_Pergunta = True
                pass
            pass

        #TODO GRAVAR id_pergunta e id_jogo NA TABELA LOG
        return pergunta
    pass

    # def get(self, request):
    #     print request.user.id
    #     print '*******************************************************************************'
    #     # data = {
    #     #     'id': request.user.id,
    #     #     'pergunta': request
    #     # }
    #     return Response('oi', status=status.HTTP_200_OK)
        


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

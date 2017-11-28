from pergunta.models import Pergunta , Alternativa
from jogo.models import Jogo, PontosTimer, JogoPerguntas
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
            return Response(data={-1:'alternativa invalida para esta pergunta'},status=status.HTTP_200_OK) #HTTP_400_BAD_REQUEST)

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
    """
    Consulta uma pergunta a partir do seu id (AdminOnly)
    """
    permission_classes = (IsAdmin, )
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaRandomView(ListAPIView):  #/random
    """
    Traz uma nova pergunta para o usuario responder
    """
    permission_classes= (IsAuthenticated,)
    serializer_class = PerguntaSerializer

    def SortearPergunta(self, pk):
        try:
            pergunta = Pergunta.objects.filter(pk=pk)
        except ObjectDoesNotExist:
            pergunta = None
        return pergunta

    def SalvarPergunta(self, jogo_id, pergunta):
        JogoPerguntas.objects.create(jogo_id=jogo_id,id_pergunta=pergunta)

    def ObterPerguntasUsadas(self, jogo):
        return JogoPerguntas.objects.filter(jogo_id=jogo.id).values_list('id_pergunta',flat=True)        

    def ObterJogo(self, usuario_id):
        try:
            jogo = Jogo.objects.get(usuario_id=usuario_id, is_active=True)
        except ObjectDoesNotExist:
            jogo = Jogo.objects.create(usuario_id=usuario_id, is_active=True)
            usuario = Usuario.objects.get(usuario_id=usuario_id) 
            #AJUSTA OS PONTOS PARA UM NOVO JOGO
            usuario.pontos = 50 if usuario.pontos < 50 else usuario.pontos
        return jogo

    def get_queryset(self):

        jogo = self.ObterJogo(self.request.user.id)
        perguntas_usadas = self.ObterPerguntasUsadas(jogo)
        perguntas_possiveis = Pergunta.objects.values_list('id_pergunta',flat=True).exclude(id_pergunta__in=perguntas_usadas)
        pk = random.choice(perguntas_possiveis)        

        pergunta = self.SortearPergunta(pk)        
        self.SalvarPergunta(jogo.id, pergunta.get())
        
        return pergunta       

class AlternativaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from pergunta.models import Pergunta , Alternativa
from pergunta.serializers import PerguntaSerializer, AlternativaSerializer,AlternativaRespostaSerializer
import random as rand

class PerguntaAlternativaView(RetrieveAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaRespostaSerializer

    def get(self, request, id_alternativa, id_pergunta):
        serializer = self.get_serializer(data=request.data)

        respostaBD = Alternativa.objects.filter(id_pergunta=id_pergunta,id_alternativa=id_alternativa).get().resposta

        if respostaBD=='1':
            return Response(data={1:'Resposta Correta!'},status=status.HTTP_200_OK)
        else:
            return Response(data={0:'Resposta Errada!'},status=status.HTTP_200_OK)


class PerguntaCreateView(ListCreateAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaListView(ListCreateAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaRandomView(ListAPIView):
    serializer_class = PerguntaSerializer

    def get_queryset(self):
        pk = rand.randint(1,300)
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

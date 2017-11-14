from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView, RetrieveAPIView

from pergunta.models import Pergunta , Alternativa
from pergunta.serializers import PerguntaSerializer, AlternativaSerializer
import random as rand


# class UserCreateView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = PerguntaSerializer


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
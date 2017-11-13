# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView, RetrieveAPIView

# from api.models import Pergunta
# from api.serializers import PerguntaSerializer
# import random as rand

# class PerguntaCreateView(ListCreateAPIView):
#     queryset = Pergunta.objects.all()
#     serializer_class = PerguntaSerializer

# class PerguntaListView(ListAPIView):
#     queryset = Pergunta.objects.all()
#     serializer_class = PerguntaSerializer

# class PerguntaDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Pergunta.objects.all()
#     serializer_class = PerguntaSerializer

# class PerguntaRandomView(ListAPIView):
#     serializer_class = PerguntaSerializer

#     def get_queryset(self):
#         pk = rand.randint(1,300)
#         #implementar busca das perguntas ja processadas
#         return Pergunta.objects.filter(pk=pk)
#     pass

        
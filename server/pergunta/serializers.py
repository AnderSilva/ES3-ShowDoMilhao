from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import serializers
from pergunta.models import Pergunta, Alternativa
# from pergunta.serializers import AlternativaSerializer


class AlternativaSerializer(ModelSerializer):
    class Meta:
        model = Alternativa
        # fields = ('id_alternativa', 'id_pergunta', 'alternativa','resposta')
        fields = ('id_alternativa','alternativa','resposta')
        extra_kwargs = {
            'id_pergunta': {'read_only': True},
            'id_alternativa': {'read_only': True}
        }


class PerguntaSerializer(ModelSerializer):
    # alternativas = serializers.ReadonlyField(many=True,read_only=True) #, view_name='alternativa_detail', read_only=True)
    # alternativas = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    alternativas = AlternativaSerializer(many=True)
    class Meta:
        model = Pergunta
        fields = ('id_pergunta','pergunta','alternativas')
        extra_kwargs = {
            'id_pergunta': {'read_only': True}
        }
    pass



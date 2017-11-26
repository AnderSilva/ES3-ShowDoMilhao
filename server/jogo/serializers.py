from rest_framework import serializers
from jogo.models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ('id','id_usuario','continente','perguntas_corretas','is_active')
        extra_kwargs = {
             'id': {'read_only': True},
             'id_usuario': {'read_only': True}
        }

from rest_framework import serializers
from jogo.models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ('id','usuario','continente','acertos','is_active')
        extra_kwargs = {
             'id': {'read_only': True},
             'usuario_id': {'read_only': True}
        }

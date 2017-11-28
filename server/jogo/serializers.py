from rest_framework import serializers
from jogo.models import Jogo, JogoPerguntas

class JogoPerguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = JogoPerguntas
        fields = ('jogo','id_pergunta', 'acertou')
        extra_kwargs = {
             'jogo': {'read_only': True},
             'id_pergunta': {'read_only': True}
        }


class JogoFilterListSerializer(serializers.ListSerializer):

	def to_representation(self, data):
		data = data.filter(is_active=True)
		return super(JogoFilterListSerializer, self).to_representation(data)


class JogoSerializer(serializers.ModelSerializer):
	jogo_perguntas = JogoPerguntasSerializer(many=True)

	class Meta:
		list_serializer_class = JogoFilterListSerializer
		model = Jogo
		fields = ('usuario','continente','acertos','is_active', 'jogo_perguntas')
		extra_kwargs = {
			# 'id': {'read_only': True},
			'usuario_id': {'read_only': True}
		}
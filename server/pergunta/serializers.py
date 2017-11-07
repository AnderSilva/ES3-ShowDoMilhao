from rest_framework.serializers import ModelSerializer

from api.models import Pergunta

class PerguntaSerializer(ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ('id_pergunta', 'pergunta')
        extra_kwargs = {
            'id_pergunta': {'read_only': True}
        }

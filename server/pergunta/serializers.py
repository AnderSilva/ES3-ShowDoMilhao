from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import serializers
from pergunta.models import Pergunta, Alternativa
from django.db import transaction

class AlternativaSerializer(ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('id_pergunta','id_alternativa', 'alternativa','resposta')
        extra_kwargs = {
             'id_pergunta': {'read_only': True},
             'id_alternativa': {'read_only': True}
        }


class PerguntaSerializer(ModelSerializer):    
    alternativas = AlternativaSerializer(many=True)
    class Meta:
        model = Pergunta
        fields = ('id_pergunta','pergunta','alternativas')
        extra_kwargs = {
            'id_pergunta': {'read_only': True}
        }
    pass

    def create(self, validated_data):
        alternativas_data = validated_data.pop('alternativas')

        with transaction.atomic():
            pergunta = Pergunta(pergunta=validated_data.pop('pergunta'))
            pergunta.clean()
            pergunta.save()

            for alternativa_data in alternativas_data:
                Alternativa.objects.filter(id_pergunta=pergunta.id_pergunta).update_or_create(id_pergunta_id=pergunta.id_pergunta,alternativa=alternativa_data['alternativa'],resposta=alternativa_data['resposta'])

        return pergunta

    def update(self, instance, validated_data):
        alternativas = validated_data.pop('alternativas')
        instance.pergunta = validated_data.pop('pergunta')
        instance.alternativas.filter(id_pergunta=instance.id_pergunta).delete()

        #Recria os itens
        for alternativa in alternativas:
            instance.alternativas.create(id_pergunta=instance.id_pergunta\
                                        ,alternativa=alternativa['alternativa']\
                                        ,resposta=alternativa['resposta'])
        instance.save()
        return instance
    pass

class AlternativaRespostaSerializer(ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('id_pergunta','id_alternativa','resposta')
        extra_kwargs = {
             'id_pergunta': {'read_only': True},
             'id_alternativa': {'read_only': True},
             'resposta': {'read_only': True}
        }

# class PerguntaAlternativaSerializer(ModelSerializer):
#     alternativas = AlternativaRespostaSerializer(many=True)
#     class Meta:
#         model = Pergunta
#         fields = ('alternativas',)
#         extra_kwargs = {
#             'id_pergunta': {'read_only': True}
#         }
#     pass

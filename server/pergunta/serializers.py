from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import serializers
from pergunta.models import Pergunta2 as Pergunta, Alternativa2 as Alternativa
# from pergunta.serializers import AlternativaSerializer
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
    # alternativas = serializers.ReadonlyField(many=True,read_only=True) #, view_name='alternativa_detail', read_only=True)    
    #alternativas = serializers.StringRelatedField(many=True,read_only=True)
    # alternativas = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name='alternativa_detail')
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

        # deletar
        instance.alternativas.filter(id_pergunta=instance.id_pergunta).delete()
        #Recria os itens
        for alternativa in alternativas:
            instance.alternativas.create(id_pergunta=instance.id_pergunta\
                                        ,alternativa=alternativa['alternativa']\
                                        ,resposta=alternativa['resposta'])


        # for alternativa in alternativas:                
        #     tupla_alternativas = instance.alternativas.get_or_create(alternativa=alternativa['alternativa'])
        #     addAlternativa = tupla_alternativas[1]

        #     if addAlternativa:
        #         print 'criar novo\n\n\n'
        #         instance.alternativas\
        #             .create(id_pergunta=instance.id_pergunta\
        #                    ,alternativa=alternativa['alternativa'])
        #     else:
        #         print 'update \n\n\n'
        #         instance.alternativas\
        #             .filter(id_pergunta=instance.id_pergunta\
        #                    ,id_alternativa=tupla_alternativas[0].id_alternativa)\
        #             .update(alternativa=alternativa['alternativa'])
   
        instance.save()
        return instance
    pass


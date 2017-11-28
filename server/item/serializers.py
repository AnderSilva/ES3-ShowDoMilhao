from rest_framework import serializers
from item.models import Item, UsuarioItem

class UsuarioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioItem
        fields = ('usuario','item', 'qtde')
        extra_kwargs = {
             'usuario': {'read_only': True},
             'item': {'read_only': True}
        }

class ItemSerializer(serializers.ModelSerializer):

	class Meta:		
		model = Item
		fields = ('nome','valor')
		

# class ItensComprarSerializer(serializers.ModelSerializer):
# 	class Meta:
#         model = UsuarioItem
#         fields = ('usuario','item', 'qtde')
#         extra_kwargs = {
#              'usuario': {'read_only': True},
#              'item': {'read_only': True}
#         }
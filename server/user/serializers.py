from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from rest_framework.views import APIView
from user.models import Usuario
from jogo.models import Jogo
from jogo.serializers import JogoSerializer
from item.serializers import UsuarioItemSerializer


class UserStatusSerializer(serializers.ModelSerializer):
    jogo_user = JogoSerializer(many=True)
    usuario_itens = UsuarioItemSerializer(many=True)


    class Meta:
        model = Usuario
        fields = ('email','username','nome','sobrenome', 'avatar'
                  ,'balao','pontos','balao','is_admin','usuario_itens','jogo_user')
        # extra_kwargs = {
        #     'usuario_id': {'read_only': True}
        # }
    pass

class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('email','username','nome','sobrenome', 'avatar'
                  ,'balao','pontos','balao','is_admin')
        # extra_kwargs = {
        #     'id': {'read_only': True}
        # }
    pass

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Usuario
        fields = ('id','nome','sobrenome', 'email','username','password','confirm_password','avatar','pontos','balao', 'is_admin')#, 'is_active')
        extra_kwargs = {
             'id': {'read_only': True}
        }

    def create(self, validated_data):        
        username=validated_data.pop('username')
        email=validated_data.pop('email')
        password=validated_data.pop('password')        
        
        return Usuario.objects.create_user(username, email, password,**validated_data)

    def update(self, instance, validated_data):
        instance.email     = validated_data.get('email'    , instance.email)
        instance.username  = validated_data.get('username' , instance.username)
        instance.nome      = validated_data.get('nome'     , instance.nome)
        instance.sobrenome = validated_data.get('sobrenome', instance.sobrenome)
        password           = validated_data.get('password'        , None)
        confirm_password   = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)
        # instance.save()
        instance = super().update(instance, validated_data)
        return instance

    def validate(self, data):
        if not (data['password'] and data['password'] == data['confirm_password']):
            raise serializers.ValidationError('As senhas devem ser iguais.')
        if 'confirm_password' in data:
            del data['confirm_password']
        return data



    # def validate(self, attrs):
    #     self.user = authenticate(login=attrs.get("login"), senha=attrs.get('senha'))
    #     if self.user:
    #         if not self.user.is_active:
    #             raise serializers.ValidationError(self.error_messages['inactive_account'])
    #         return attrs
    #     else:
    #         raise serializers.ValidationError(self.error_messages['invalid_credentials'])




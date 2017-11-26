from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from rest_framework.views import APIView
from user.models import Usuario
from jogo.models import Jogo
from jogo.serializers import JogoSerializer


class UserStatusSerializer(serializers.ModelSerializer):    
    jogo_user = JogoSerializer(many=True)
    class Meta:
        model = Usuario
        fields = ('nome','sobrenome', 'email','username','avatar','pontos','balao','jogo_user')
        # extra_kwargs = {
        #     'id': {'read_only': True}
        # }
    pass


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ('id','nome','sobrenome', 'email','username','password','confirm_password','avatar','pontos','balao')#, 'is_active')
        extra_kwargs = {
             'id': {'read_only': True}
        }

    def create(self, validated_data):
        print type(validated_data)
        print '***********************************************'
        username=validated_data.pop('username')
        email=validated_data.pop('email')
        password=validated_data.pop('password')
        # return Usuario.objects.create_user(**validated_data)
        return Usuario.objects.create_user(username, email, password, **validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('email', instance.username)
        instance.nome = validated_data.get('email', instance.nome)
        instance.sobrenome = validated_data.get('email', instance.sobrenome)
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate(self, data):
        if not (data['password'] and data['password'] == data['confirm_password']):
            raise serializers.ValidationError('As senhas devem ser iguais.')
        data.pop('confirm_password')
        return data



    # def validate(self, attrs):
    #     self.user = authenticate(login=attrs.get("login"), senha=attrs.get('senha'))
    #     if self.user:
    #         if not self.user.is_active:
    #             raise serializers.ValidationError(self.error_messages['inactive_account'])
    #         return attrs
    #     else:
    #         raise serializers.ValidationError(self.error_messages['invalid_credentials'])




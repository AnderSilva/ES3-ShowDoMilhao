from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import serializers
from user.models import Usuario
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome','sobrenome', 'email','login','senha','is_admin')
        extra_kwargs = {
             'id_usuario': {'read_only': True}             
        }


class UserLoginSerializer(ModelSerializer):
    login = serializers.CharField(required=True)
    senha = serializers.CharField(required=True)

    # default_error_messages = {
    #     'inactive_account': _('Usuario esta desativado.'),
    #     'invalid_credentials': _('Impossibilidade de login com as credenciais fornecidas.')
    # }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    class Meta:
        model = Usuario
        fields = ('login','senha')
        extra_kwargs = {
             'id_usuario': {'read_only': True}
        }

    # def validate(self, attrs):
    #     self.user = authenticate(login=attrs.get("login"), senha=attrs.get('senha'))
    #     if self.user:
    #         if not self.user.is_active:
    #             raise serializers.ValidationError(self.error_messages['inactive_account'])
    #         return attrs
    #     else:
    #         raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token",)
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from core.users.models import Usuario
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UsuarioRegistrationSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ("id", "email", "senha", "confirm_password")

    def create(self, validated_data):
        del validated_data["confirm_password"]
        return super(UsuarioRegistrationSerializer, self).create(validated_data)

    def validate(self, attrs):
        if attrs.get('senha') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Senhas nao conferem.")
        return attrs


class UsuarioLoginSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    senha = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': _('Usuario esta desativado.'),
        'invalid_credentials': _('Impossibilidade de login com as credenciais fornecidas.')
    }

    def __init__(self, *args, **kwargs):
        super(UsuarioLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(login=attrs.get("login"), password=attrs.get('senha'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token",)

# from django.db import models
#
# class Usuario(models.Model):
#     id_usuario = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=255)
#     sobrenome = models.CharField(max_length=255)
#     email = models.CharField(max_length=255,unique=True)
#     login = models.CharField(max_length=255)
#     senha = models.CharField(max_length=255)
#     avatar = models.IntegerField()
#     balao = models.IntegerField()
#     pontos = models.IntegerField()
#     is_admin = models.BooleanField()
#     inativo = models.BooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'usuario'

import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_admin, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
          raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,
                 is_admin=is_admin, is_active=True,
                 is_superuser=is_superuser, last_login=now,
                 date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        # extra_fields.get('')

        return self._create_user(username, email, password,False, False,
                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True,
                 **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True,
        help_text=_('Obrigatorio. Ate 15 caracteres. Letras, \
                    numeros e @/./+/-/_ caracteres'),
        validators=[
                    validators.RegexValidator(
                                            re.compile('^[\w.@+-]+$'),
                                            _('Entre um username valido.'),
                                            _('invalido'))])
    email = models.EmailField(_('email'), max_length=255, unique=True)
    nome = models.CharField(_('nome'), max_length=255)
    sobrenome = models.CharField(_('sobrenome'), max_length=255)
    avatar = models.IntegerField(default=1)
    balao = models.IntegerField(default=1)
    pontos = models.IntegerField(default=50)
    is_admin = models.BooleanField(_('status Admin'), default=False,
        help_text=_('Flag que define se o usuario pode acessar area Administrativa.'))
    is_active = models.BooleanField(_('ativo'), default=True,
        help_text=_('Flag que define se o usuario esta ativo. \
                    Desmarque a opcao no lugar de deletar o usuario.'))
    date_joined = models.DateTimeField(_('data criacao'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
        help_text=_('Quando o usuario confirmar a conta.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'usuario'
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_full_name(self):
        full_name = '%s %s' % (self.nome, self.sobrenome)
        return full_name.strip()

    def get_short_name(self):
        return self.nome

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

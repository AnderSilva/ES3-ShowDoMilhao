from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Pergunta2(models.Model):
    id_pergunta = models.AutoField(primary_key=True)
    pergunta = models.CharField(max_length=1000)    

    class Meta:
        managed = True
        db_table = 'pergunta2'

class Alternativa2(models.Model):
    id_alternativa = models.AutoField(primary_key=True)
    id_pergunta = models.ForeignKey(Pergunta2, db_column='id_pergunta',related_name='alternativas',on_delete=models.CASCADE)
    alternativa = models.CharField(max_length=1000)
    resposta = models.IntegerField()  # This field type is a guess.
    frequencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'alternativa2'

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    avatar = models.IntegerField()
    balao = models.IntegerField()
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=6)
    pontos = models.IntegerField()
    is_admin = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usuario'

class RespostaUsuario(models.Model):
    id_resposta = models.AutoField(primary_key=True)
    id_pergunta = models.ForeignKey(Pergunta2, db_column='id_pergunta', related_name='perguntas',on_delete=models.CASCADE,blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario, db_column='id_usuario',related_name='usuarios')
    id_alternativa = models.IntegerField()
    verifica = models.IntegerField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    pontos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resposta_usuario'


# class Pergunta(models.Model):
#     id_pergunta = models.IntegerField(primary_key=True)
#     pergunta = models.CharField(max_length=1000)


#     class Meta:
#         managed = False
#         db_table = 'pergunta'

# class Alternativa(models.Model):
#     id_alternativa = models.IntegerField(primary_key=True)
#     id_pergunta = models.ForeignKey('Pergunta', db_column='id_pergunta',related_name='alternativas')
#     alternativa = models.CharField(max_length=1000)
#     resposta = models.TextField()  # This field type is a guess.
#     frequencia = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'alternativa'
    
    # def __unicode__(self):
    #     return '%d: %s : %s' % (self.id_alternativa, self.alternativa, self.resposta)




# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password,
#                      is_staff, is_superuser, **extra_fields):
#         """
#         Creates and saves a User with the given username, email and password.
#         """
#         now = timezone.now()
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email,
#                           is_staff=is_staff, is_active=True,
#                           is_superuser=is_superuser,
#                           date_joined=now, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         return self._create_user(email, password, False, False,
#                                  **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         return self._create_user(email, password, True, True,
#                                  **extra_fields)

# class BaseUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     is_staff = models.BooleanField(_('staff status'), default=False,
#                                    help_text=_('Designates whether the user can log into this admin '
#                                                'site.'))
#     is_active = models.BooleanField(_('active'), default=True,
#                                     help_text=_('Designates whether this user should be treated as '
#                                                 'active. Unselect this instead of deleting accounts.'))
#     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         """
#         Returns the first_name plus the last_name, with a space in between.
#         """
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         "Returns the short name for the user."
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         """
#         Sends an email to this User.
#         """
#         send_mail(subject, message, from_email, [self.email], **kwargs)

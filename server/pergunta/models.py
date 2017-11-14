from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Pergunta(models.Model):
    id_pergunta = models.AutoField(primary_key=True)
    pergunta = models.CharField(max_length=1000)    

    class Meta:
        managed = False
        db_table = 'pergunta2'

class Alternativa(models.Model):
    id_alternativa = models.AutoField(primary_key=True)
    id_pergunta = models.ForeignKey(Pergunta, db_column='id_pergunta',related_name='alternativas',on_delete=models.CASCADE)
    alternativa = models.CharField(max_length=1000)
    resposta = models.IntegerField()  # This field type is a guess.
    frequencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alternativa2'


# class RespostaUsuario(models.Model):
#     id_resposta = models.AutoField(primary_key=True)
#     id_pergunta = models.ForeignKey(Pergunta, db_column='id_pergunta', related_name='perguntas',on_delete=models.CASCADE,blank=True, null=True)
#     id_usuario = models.ForeignKey(User, db_column='id_usuario',related_name='usuarios')
#     id_alternativa = models.IntegerField()
#     verifica = models.IntegerField(blank=True, null=True)
#     tempo = models.FloatField(blank=True, null=True)
#     pontos = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'resposta_usuario'


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


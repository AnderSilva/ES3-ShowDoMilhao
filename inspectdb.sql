# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Alternativas(models.Model):
    id_alternativa = models.IntegerField(db_column='ID_ALTERNATIVA')  # Field name made lowercase.
    id_pergunta = models.ForeignKey('Perguntas', db_column='ID_PERGUNTA')  # Field name made lowercase.
    alternativa = models.CharField(db_column='ALTERNATIVA', max_length=1000)  # Field name made lowercase.
    resposta = models.IntegerField(db_column='RESPOSTA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALTERNATIVAS'
        unique_together = (('ID_PERGUNTA', 'ID_ALTERNATIVA'),)


class Perguntas(models.Model):
    id_pergunta = models.AutoField(db_column='ID_PERGUNTA', primary_key=True)  # Field name made lowercase.
    pergunta = models.CharField(db_column='PERGUNTA', max_length=1000)  # Field name made lowercase.
    estado = models.IntegerField(db_column='ESTADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERGUNTAS'


class RespostaUsuario(models.Model):
    id_resposta = models.AutoField(db_column='ID_RESPOSTA', primary_key=True)  # Field name made lowercase.
    id_pergunta = models.ForeignKey(Perguntas, db_column='ID_PERGUNTA')  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', db_column='ID_USUARIO')  # Field name made lowercase.
    id_alternativa = models.IntegerField(db_column='ID_ALTERNATIVA')  # Field name made lowercase.
    verifica = models.IntegerField(db_column='VERIFICA')  # Field name made lowercase.
    tempo = models.FloatField(db_column='TEMPO', blank=True, null=True)  # Field name made lowercase.
    pontos = models.IntegerField(db_column='PONTOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESPOSTA_USUARIO'


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_USUARIO', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    sobrenome = models.CharField(db_column='SOBRENOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=40)  # Field name made lowercase.
    avatar = models.IntegerField(db_column='AVATAR', blank=True, null=True)  # Field name made lowercase.
    balao = models.IntegerField(db_column='BALAO', blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=6)  # Field name made lowercase.
    pontos = models.IntegerField(db_column='PONTOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO'

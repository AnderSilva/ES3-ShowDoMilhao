from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    avatar = models.IntegerField()
    balao = models.IntegerField()
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    pontos = models.IntegerField()
    is_admin = models.BooleanField()  # This field type is a guess.
    inativo = models.BooleanField()  # This field type is a guess.


    class Meta:
        managed = False
        db_table = 'usuario'

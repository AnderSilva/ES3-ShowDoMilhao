from django.db import models

# Create your models here.
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
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db       import models
from user.models     import Usuario
from pergunta.models import Pergunta

class Jogo(models.Model):
    id_usuario    = models.ForeignKey(Usuario , db_column='id_Usuario' ,related_name='jogo_user',on_delete=models.CASCADE)
    continente = models.IntegerField(null=False,default=1,validators=[MinValueValidator(1),MaxValueValidator(6)]) #numero entre  1 e 6    
    perguntas_corretas = models.IntegerField(null=False,default=0)
    last_update = models.DateTimeField(auto_now=True)
    is_active   = models.BooleanField(default=True,null=False)

    class Meta:
        managed = True
        db_table = 'jogo'
        verbose_name = _('jogo')
        verbose_name_plural = _('jogos')

from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db       import models
from user.models     import Usuario

class Jogo(models.Model):
    usuario     = models.ForeignKey(Usuario , db_column='id_Usuario' ,related_name='jogo_user',on_delete=models.CASCADE)
    continente  = models.IntegerField(null=False,default=1,validators=[MinValueValidator(1),MaxValueValidator(6)]) #numero entre  1 e 6    
    acertos     = models.IntegerField(null=False,default=0)    
    last_update = models.DateTimeField(auto_now=True)
    is_active   = models.BooleanField(default=True,null=False)

    class Meta:
        managed = True
        db_table = 'jogo'
        verbose_name = _('jogo')
        verbose_name_plural = _('jogos')

    def save(self, *args, **kwargs):        
        aux = (self.acertos / 5) +1
        aux = 7 if aux > 7 else aux
        self.continente = aux
        super(Jogo, self).save(*args, **kwargs)

class PontosTimer(models.Model):    
    ate_segundos = models.IntegerField()
    pontos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pontos_timer'

from django.db 		import models
from user.models    import Usuario

class Item(models.Model):	
    nome  = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'item'


class UsuarioItem(models.Model):
    usuario = models.ForeignKey(Usuario)
    item = models.ForeignKey(Item)
    qtde = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_item'
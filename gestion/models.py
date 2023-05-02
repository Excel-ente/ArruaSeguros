from django.db import models
from administracion.models import *
import datetime
from datetime import timedelta

ESTADO = [ # -- LISTA CHOICES OPERATIVOS
    ("Vigente","Vigente"),
    ("Vencida","Vencida"),
    ("Inactivo","Inactivo"),
]

ESTADO_SINIESTRO = [ # -- LISTA CHOICES OPERATIVOS
    ("Recibido","Recibido"),
    ("En Proceso","En Proceso"),
    ("En Espera","En Espera"),
    ("Finalizado","Finalizado"),
]

class Poliza(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.PROTECT,blank=False,null=False)
    cobertura=models.ForeignKey(Cobertura,on_delete=models.PROTECT,blank=False,null=False)
    bien=models.ForeignKey(Bien,on_delete=models.PROTECT,blank=False,null=False)
    fecha_inicio=models.DateField(default=datetime.datetime.now,null=True, blank=True)
    fecha_vencimiento=models.DateField(default=datetime.datetime.now,null=True, blank=True)
    estado=models.CharField(max_length=20,choices=ESTADO,default="Vigente",blank=True,null=True)
    comentarios=models.TextField(blank=True,null=True)
    actualizaciones=models.IntegerField(default=1,null=True,blank=True)

    def __str__(self):

        return f"{self.cliente} | {self.cobertura} - Bien: {self.bien} Vence el {self.fecha_vencimiento} "



    def save(self, *args, **kwargs):

        dias = self.cobertura.plazo_en_dias * self.actualizaciones

        self.fecha_vencimiento = self.fecha_inicio + timedelta(days=dias)

        super().save(*args, **kwargs)

    
class Siniestro(models.Model):
    fecha_siniestro=models.DateField(default=datetime.datetime.now,null=False, blank=False)
    poliza_cliente=models.ForeignKey(Poliza,on_delete=models.PROTECT,blank=False,null=False)
    cliente=models.CharField(max_length=255,blank=True,null=True)
    vencimiento_siniestro=models.DateField(default=datetime.datetime.now,null=False, blank=False)
    estado=models.CharField(max_length=20,choices=ESTADO_SINIESTRO,default="Recibido",blank=False,null=False)
    nombre_tercero=models.CharField(max_length=255,blank=False,null=False)
    documento_tercero=models.CharField(max_length=255,blank=False,null=False)
    compania_tercero=models.CharField(max_length=255,blank=False,null=False)
    poliza_tercero=models.CharField(max_length=255,blank=False,null=False)
    patente_tercero=models.CharField(max_length=255,blank=False,null=False)
    vehiculo_tercero=models.CharField(max_length=255,blank=False,null=False)
    lugar_tercero=models.CharField(max_length=255,blank=False,null=False)
    localidad_tercero=models.CharField(max_length=255,blank=False,null=False)
    telefono_tercero=models.CharField(max_length=255,blank=False,null=False)
    comentarios=models.TextField(blank=True,null=True)

    def __str__(self):

        return f"{self.cliente} | {self.nombre_tercero} - Estado: {self.estado} Vencimiento {self.vencimiento_siniestro} "


    def save(self, *args, **kwargs):

        self.cliente = self.poliza_cliente.cliente.nombre

        super().save(*args, **kwargs)
 
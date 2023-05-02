from datetime import date
from django.utils import timezone
from django_crontab import crontab
from .models import Poliza

@crontab('0 0 * * *')  # Ejecutar a medianoche todos los días
def actualizar_pólizas_vencidas():
    polizas_vencidas = Poliza.objects.filter(fecha_vencimiento__lte=timezone.now().date())
    for poliza in polizas_vencidas:
        poliza.estado = 'Vencida'
        poliza.save()

#esta funcion es la que actualiza las polizas todos los dias a las 00:00

# despues, cuando la fucion corra, vamos a armar un mail tipo reporte para que reciba el usuario con las polizas por vencer.
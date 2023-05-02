from django.contrib import admin
from .models import Poliza,Siniestro


@admin.register(Poliza)
class PolizaAdmin(admin.ModelAdmin):
    list_display=('cliente','cobertura','bien','fecha_vencimiento','estado',)
    exclude=('fecha_vencimiento','estado',)


@admin.register(Siniestro)
class PolizaAdmin(admin.ModelAdmin):
    list_display=('fecha_siniestro','estado','cliente','compania_tercero','vencimiento_siniestro',)
    exclude=('cliente','estado',)

    
from django.contrib import admin
from api.models import TiposAtributos


# Register your models here.
class TiposAtributosAdmin(admin.ModelAdmin):
    pass

admin.site.register(TiposAtributos, TiposAtributosAdmin)

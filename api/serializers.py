from rest_framework import serializers

from api.models import TiposAtributos

class TiposAtributosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposAtributos
        fields = ('id', 'codigo', 'descripcion')

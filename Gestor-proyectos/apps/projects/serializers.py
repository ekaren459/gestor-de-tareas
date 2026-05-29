from rest_framework import serializers
from .models import Columna, Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'


class ColumnaSerializer(serializers.ModelSerializer):
    tarjetas = TarjetaSerializer(many=True, read_only=True)

    class Meta:
        model = Columna
        fields = '__all__'

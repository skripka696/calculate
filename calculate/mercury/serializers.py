from rest_framework import serializers
from .models import Currency


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('name', 'symbol', 'price_in_usd')

from rest_framework import serializers
from .models import Companhia_Aerea, Aviao, Voo_Nacional, Voo_Internacional

class CompanhiaAereaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companhia_Aerea
        fields = '__all__'

class AviaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviao
        fields = '__all__'

class VooNacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo_Nacional
        fields = '__all__'

class VooInternacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo_Internacional
        fields = '__all__'

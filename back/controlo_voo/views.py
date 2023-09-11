from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework import viewsets
from rest_framework import generics
from .models import Companhia_Aerea, Aviao, Voo_Nacional, Voo_Internacional
from .serializers import CompanhiaAereaSerializer, AviaoSerializer, VooNacionalSerializer, VooInternacionalSerializer
from .forms import *

# Define your views and use the corresponding serializers.

class AviaoView(viewsets.ModelViewSet):
    queryset = Aviao.objects.all()
    serializer_class = AviaoSerializer

class CompanhiaView(viewsets.ModelViewSet):
    serializer_class = CompanhiaAereaSerializer
    queryset = Companhia_Aerea.objects.all()

class NacionalView(viewsets.ModelViewSet):
    serializer_class = VooNacionalSerializer
    queryset = Voo_Nacional.objects.all()

class CreateNacional(generics.CreateAPIView):
    queryset = Voo_Nacional.objects.all()
    serializer_class = VooNacionalSerializer

class CreateAviao(generics.CreateAPIView):
    queryset = Aviao.objects.all()
    serializer_class = AviaoSerializer

class CreateInternacional(generics.CreateAPIView):
    queryset = Voo_Internacional.objects.all()
    serializer_class = VooInternacionalSerializer

class CreateCompanhia(generics.CreateAPIView):
    queryset = Companhia_Aerea.objects.all()
    serializer_class = CompanhiaAereaSerializer

class InternacionalView(viewsets.ModelViewSet):
    serializer_class = VooInternacionalSerializer
    queryset = Voo_Internacional.objects.all()

def delete_aviao(request, id):
    if request.method == 'POST':
        aviao = Aviao.objects.get(pk=id)
        aviao.delete()
    return HttpResponseRedirect(reverse('index'))

def delete_internacional(request, id):
    if request.method == 'POST':
        internacional = Voo_Internacional.objects.get(pk=id)
        internacional.delete()
    return HttpResponseRedirect(reverse('index'))

def delete_nacional(request, id):
    if request.method == 'POST':
        nacional = Voo_Nacional.objects.get(pk=id)
        nacional.delete()
    return HttpResponseRedirect(reverse('index'))

def delete_companhia(request, id):
    if request.method == 'POST':
        companhia = Companhia_Aerea.objects.get(pk=id)
        companhia.delete()
    return HttpResponseRedirect(reverse('index'))

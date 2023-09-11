from django.db import models

# Create your models here.

class Companhia_Aerea(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    numero_de_aeronaves = models.IntegerField()
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.codigo}"

class Aviao(models.Model):
    registro = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_de_passageiros = models.IntegerField()

    def __str__(self):
        return f"{self.registro}"

class Voo_Nacional(models.Model):
    codigo = models.CharField(max_length=10)
    entrante = models.BooleanField(default=False)
    id_companhia_aerea = models.ForeignKey(Companhia_Aerea, on_delete=models.CASCADE)
    cidadeD = models.CharField(max_length=100)
    cidadeO = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    id_aviao = models.ForeignKey(Aviao, on_delete=models.CASCADE)

class Voo_Internacional(Voo_Nacional):
    pais_destino = models.CharField(max_length=50)
    numero_paises = models.IntegerField()

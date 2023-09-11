from django.contrib import admin
from .models import Aviao, Companhia_Aerea, Voo_Internacional, Voo_Nacional


# Register your models here.
admin.site.register({Aviao, Companhia_Aerea, Voo_Internacional, Voo_Nacional})
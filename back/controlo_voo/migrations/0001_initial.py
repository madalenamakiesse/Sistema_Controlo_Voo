# Generated by Django 4.2.5 on 2023-09-05 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aviao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('registro', models.CharField(max_length=20)),
                ('numero_de_passageiros', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Companhia_Aerea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=100)),
                ('numero_de_aeronaves', models.IntegerField()),
                ('nacionalidade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Voo_Nacional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('entrante', models.BooleanField(default=False)),
                ('cidadeD', models.CharField(max_length=100)),
                ('cidadeO', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('id_aviao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlo_voo.aviao')),
                ('id_companhia_aerea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlo_voo.companhia_aerea')),
            ],
        ),
        migrations.CreateModel(
            name='Voo_Internacional',
            fields=[
                ('voo_nacional_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='controlo_voo.voo_nacional')),
                ('pais_destino', models.CharField(max_length=50)),
                ('numero_paises', models.IntegerField()),
            ],
            bases=('controlo_voo.voo_nacional',),
        ),
    ]

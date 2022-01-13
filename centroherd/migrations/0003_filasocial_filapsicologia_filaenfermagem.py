# Generated by Django 4.0.1 on 2022-01-13 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centroherd', '0002_alter_dst_options_rename_constatado_dst_constatada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilaSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente')),
            ],
            options={
                'verbose_name': 'Fila - Serviço Social',
                'verbose_name_plural': 'Fila - Serviço Social',
            },
        ),
        migrations.CreateModel(
            name='FilaPsicologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente')),
            ],
            options={
                'verbose_name': 'Fila - Psicologia',
                'verbose_name_plural': 'Fila - Psicologia',
            },
        ),
        migrations.CreateModel(
            name='FilaEnfermagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente')),
            ],
            options={
                'verbose_name': 'Fila - Enfermagem',
                'verbose_name_plural': 'Fila - Enfermagem',
            },
        ),
    ]
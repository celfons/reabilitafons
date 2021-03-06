# Generated by Django 4.0.1 on 2022-01-18 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('centroherd', '0006_alter_paciente_convenio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='acompanhamento',
        ),
        migrations.AddField(
            model_name='paciente',
            name='cartao_sus',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='carteira_trabalho',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='reservista',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='titulo_eleitor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='social',
            name='familiar_com_historico_de_uso',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='social',
            name='modalidade_atencao_orientada',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='social',
            name='observacao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='social',
            name='possui_renda',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='problemas_causados_pela_droga',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='social',
            name='problemas_com_justica',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'N??o'), ('ns', 'N.S')], max_length=5),
        ),
        migrations.AddField(
            model_name='social',
            name='problemas_com_justica_observacao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='social',
            name='relacao_familiar',
            field=models.CharField(blank=True, choices=[('fortalecidos', 'Fortalecidos'), ('fragilizados', 'Fragilizados'), ('rompidos', 'Rompidos'), ('ns', 'N.S'), ('nr', 'N.R')], max_length=12),
        ),
        migrations.AddField(
            model_name='social',
            name='relato_caso',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='social',
            name='situacao_profissional',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='psicologia',
            name='acompanhamento',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='PlanoAcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demandas', models.TextField(blank=True)),
                ('previsao', models.DateField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.social')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Plano de A????es',
            },
        ),
        migrations.CreateModel(
            name='HistoricoTratamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(max_length=200)),
                ('periodo_inicial', models.DateField(blank=True)),
                ('periodo_final', models.DateField(blank=True)),
                ('observacao', models.TextField(blank=True)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.social')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Histortico de Tratamentos',
            },
        ),
        migrations.CreateModel(
            name='HistoricoDroga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('droga', models.CharField(choices=[('alcool', 'Alcool'), ('crack', 'Crack'), ('maconha', 'Maconha/Haxixe'), ('cocaina', 'Cocaina'), ('inalante', 'Inalante/Cola'), ('diazepan', 'Diazepan'), ('anfetamina', 'Anfetamina/Remedio p/ Emagrecer'), ('ecstasy', 'Ecstasy/MDMA'), ('lsd', 'LSD'), ('heroina', 'Heroina'), ('tabaco', 'Tabaco'), ('outros', 'Outros')], max_length=100)),
                ('quantas_vezes_interrompeu_uso', models.BigIntegerField()),
                ('observacoes', models.TextField(blank=True)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.social')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hist??rico de Drogas',
            },
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-12 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possui_doenca_cronica', models.BooleanField(null=True)),
                ('uso_medicacao_continua', models.BooleanField(null=True)),
                ('possui_alergia_medicacao', models.BooleanField(null=True)),
                ('tabagismo', models.BooleanField(null=True)),
                ('etilismo', models.BooleanField(null=True)),
                ('drogas', models.BooleanField(null=True)),
                ('familia_diabetes', models.BooleanField(null=True)),
                ('familia_hipertensao', models.BooleanField(null=True)),
                ('exame_dst', models.BooleanField(null=True)),
                ('acompanhamento', models.TextField()),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Enfermagem - Prontuario',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.BigIntegerField(unique=True)),
                ('rg', models.BigIntegerField(unique=True)),
                ('telefone', models.BigIntegerField(blank=True, null=True)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('solteiro', 'Solteiro'), ('casado', 'Casado'), ('viuvo', 'Viuvo'), ('divorciado', 'Divorciado')], max_length=15)),
                ('cor', models.CharField(blank=True, max_length=20)),
                ('filhos', models.BooleanField(null=True)),
                ('profissao', models.CharField(blank=True, max_length=100)),
                ('escolaridade', models.CharField(blank=True, choices=[('analfabeto', 'Analfabeto'), ('infantil', 'Infantil'), ('primario', 'Primario'), ('fundamental', 'Fundamental'), ('medio', 'Medio'), ('superior', 'Superior'), ('desconhecido', 'Desconhecido')], max_length=15)),
                ('pai', models.CharField(blank=True, max_length=200)),
                ('mae', models.CharField(blank=True, max_length=200)),
                ('naturalidade', models.CharField(blank=True, max_length=50)),
                ('endereco', models.CharField(blank=True, max_length=50)),
                ('bairro', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(blank=True, max_length=50)),
                ('cep', models.BigIntegerField(blank=True, null=True)),
                ('encaminhamento', models.CharField(blank=True, max_length=200)),
                ('inss', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], max_length=15)),
                ('usuario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acompanhamento', models.TextField()),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Servi??o Social - Prontuario',
            },
        ),
        migrations.CreateModel(
            name='Psicologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acompanhamento', models.TextField()),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Psicologia - Prontuario',
            },
        ),
        migrations.CreateModel(
            name='Medicacao_Continua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('enfermagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.enfermagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Medica????o Continua',
                'verbose_name_plural': 'Medica????o Continua',
            },
        ),
        migrations.AddField(
            model_name='enfermagem',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente'),
        ),
        migrations.AddField(
            model_name='enfermagem',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tratamento', models.BooleanField(null=True)),
                ('constatado', models.DateField(blank=True, null=True)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('enfermagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.enfermagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doen??a(s) Cronica',
                'verbose_name_plural': 'Doen??a Cronica',
            },
        ),
        migrations.CreateModel(
            name='Doenca_Cronica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doenca', models.CharField(choices=[('hiv', 'HIV'), ('hipertensao', 'Hipertensao'), ('diabetes', 'Diabetes'), ('outra', 'Outra')], max_length=20)),
                ('outra', models.CharField(blank=True, max_length=200)),
                ('tempo', models.CharField(blank=True, max_length=20)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('enfermagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.enfermagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doen??a(s) Cronica',
                'verbose_name_plural': 'Doen??a Cronica',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('parentesco', models.CharField(max_length=100)),
                ('telefone', models.BigIntegerField()),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Telefones de Contato',
            },
        ),
        migrations.CreateModel(
            name='Alergia_Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('criado', models.DateField(auto_now_add=True)),
                ('atualizado', models.DateField(auto_now=True)),
                ('enfermagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.enfermagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Alergia Medicamento',
                'verbose_name_plural': 'Alergia Medicamento',
            },
        ),
    ]

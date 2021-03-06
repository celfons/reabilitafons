# Generated by Django 4.0.1 on 2022-01-13 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centroherd', '0003_filasocial_filapsicologia_filaenfermagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='convenio',
            field=models.CharField(blank=True, choices=[('senapred', 'SENAPRED'), ('comad', 'COMAD')], max_length=10),
        ),
        migrations.AlterField(
            model_name='filaenfermagem',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente', unique=True),
        ),
        migrations.AlterField(
            model_name='filapsicologia',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente', unique=True),
        ),
        migrations.AlterField(
            model_name='filasocial',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centroherd.paciente', unique=True),
        ),
    ]

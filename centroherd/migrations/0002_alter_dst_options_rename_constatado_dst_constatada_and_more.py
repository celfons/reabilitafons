# Generated by Django 4.0.1 on 2022-01-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centroherd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dst',
            options={'verbose_name': 'DST', 'verbose_name_plural': 'DST'},
        ),
        migrations.RenameField(
            model_name='dst',
            old_name='constatado',
            new_name='constatada',
        ),
        migrations.RemoveField(
            model_name='doenca_cronica',
            name='tempo',
        ),
        migrations.AddField(
            model_name='doenca_cronica',
            name='constatada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enfermagem',
            name='acompanhamento',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-09 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211109_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='data_criado',
            field=models.CharField(default='09/11/2021', max_length=15, verbose_name='Data_Criado'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='data_criado',
            field=models.CharField(default='09/11/2021', max_length=15, verbose_name='Data_Criado'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data_criado',
            field=models.CharField(default='09/11/2021', max_length=15, verbose_name='Data_Criado'),
        ),
        migrations.AlterField(
            model_name='solicitacaoservico',
            name='data_criado',
            field=models.CharField(default='09/11/2021', max_length=15, verbose_name='Data_Criado'),
        ),
    ]

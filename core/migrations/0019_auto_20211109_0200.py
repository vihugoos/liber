# Generated by Django 3.2.8 on 2021-11-09 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20211109_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='finalizado',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='finalizado',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='finalizado',
        ),
    ]

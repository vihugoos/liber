# Generated by Django 3.2.8 on 2021-11-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacaoservico',
            name='id_observacao',
            field=models.IntegerField(default=813500, verbose_name='Id Observação'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_solicitacaoservico_id_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaoservico',
            name='id_observacao',
            field=models.CharField(default=33726, max_length=999999, verbose_name='Id Observação'),
        ),
    ]

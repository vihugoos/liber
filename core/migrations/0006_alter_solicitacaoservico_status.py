# Generated by Django 3.2.8 on 2021-11-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_solicitacaoservico_id_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaoservico',
            name='status',
            field=models.CharField(blank=True, choices=[('Em aberto', 'Em aberto'), ('Em andamento', 'Em andamento'), ('Concluida', 'Concluida')], default='Em aberto', max_length=13, verbose_name='Status'),
        ),
    ]

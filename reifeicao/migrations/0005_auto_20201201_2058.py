# Generated by Django 3.1.4 on 2020-12-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reifeicao', '0004_auto_20201201_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='tipo_de_refeiçao',
            new_name='tipo_de_refeicao',
        ),
        migrations.RemoveField(
            model_name='form',
            name='alunos',
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=50)),
                ('professor', models.ManyToManyField(related_name='alunos', to='reifeicao.Form')),
            ],
        ),
    ]
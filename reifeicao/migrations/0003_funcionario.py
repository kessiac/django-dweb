# Generated by Django 3.1.4 on 2020-12-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reifeicao', '0002_auto_20201201_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=50)),
            ],
        ),
    ]
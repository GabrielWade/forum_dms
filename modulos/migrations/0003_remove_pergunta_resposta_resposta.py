# Generated by Django 4.2.1 on 2023-06-25 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_pergunta_respondida_pergunta_resposta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='resposta',
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField(blank=True, null=True)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='modulos.pergunta')),
            ],
        ),
    ]

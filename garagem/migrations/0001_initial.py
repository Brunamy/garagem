# Generated by Django 4.1.7 on 2023-03-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nacionalidade', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('isin', models.CharField(max_length=12, unique=True)),
                ('ticker', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('naam', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=15)),
                ('taks', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]

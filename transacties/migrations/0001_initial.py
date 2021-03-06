# Generated by Django 3.0.7 on 2020-06-27 17:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producten', '0004_auto_20200627_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verkoop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(default=datetime.date.today)),
                ('aantal', models.IntegerField()),
                ('koers', models.DecimalField(decimal_places=5, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producten.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Dividend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(default=datetime.date.today)),
                ('bedrag', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producten.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Correctie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrag', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producten.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Aankoop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(default=datetime.date.today)),
                ('aantal', models.IntegerField()),
                ('koers', models.DecimalField(decimal_places=5, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producten.Product')),
            ],
        ),
    ]

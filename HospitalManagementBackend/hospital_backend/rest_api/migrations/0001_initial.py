# Generated by Django 3.1.3 on 2020-11-21 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('totalBeds', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.CharField(max_length=13)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('dateOfBirth', models.DateField()),
                ('height', models.DecimalField(decimal_places=3, max_digits=8)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=8)),
                ('address', models.TextField(max_length=150)),
                ('bloodGroup', models.CharField(max_length=5)),
                ('aadharCard', models.CharField(max_length=12)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.hospital')),
            ],
        ),
    ]
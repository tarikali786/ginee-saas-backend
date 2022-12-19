# Generated by Django 4.1.2 on 2022-12-02 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_name', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.CharField(blank=True, max_length=55, null=True)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(blank=True, max_length=10, null=True)),
                ('children_count', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=555, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('annual_income', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('quote', models.TextField(blank=True, null=True)),
                ('devices', models.ManyToManyField(to='personaApp.devices')),
                ('technology', models.ManyToManyField(to='personaApp.technology')),
            ],
        ),
    ]

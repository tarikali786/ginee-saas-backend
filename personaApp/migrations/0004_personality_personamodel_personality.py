# Generated by Django 4.1.2 on 2022-12-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaApp', '0003_digitalapps_personamodel_digital_apps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_field', models.CharField(blank=True, max_length=25, null=True)),
                ('max_field', models.CharField(blank=True, max_length=25, null=True)),
                ('values', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='personamodel',
            name='personality',
            field=models.ManyToManyField(to='personaApp.personality'),
        ),
    ]

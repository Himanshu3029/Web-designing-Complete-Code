# Generated by Django 4.0.3 on 2022-03-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=50)),
                ('Passward', models.CharField(max_length=10)),
                ('Adress1', models.CharField(max_length=80)),
                ('Adress2', models.CharField(max_length=60)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Pin', models.CharField(max_length=7)),
                ('date', models.DateField()),
            ],
        ),
    ]
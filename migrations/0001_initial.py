# Generated by Django 4.0.4 on 2022-05-14 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('Address', models.CharField(max_length=30)),
                ('Owner_Company', models.CharField(max_length=20)),
                ('Zip_Code', models.CharField(max_length=10)),
                ('Building_ID', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('Unit_ID', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True)),
                ('Unit_Type', models.CharField(max_length=20)),
                ('Building_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.building')),
            ],
        ),
    ]

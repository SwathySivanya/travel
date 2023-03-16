# Generated by Django 4.1.7 on 2023-03-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
            options={
                'db_table': 'cafeapp_place',
            },
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='pics')),
                ('dis', models.TextField()),

            ],
            options={
                'db_table': 'cafeapp_team',
            },

        ),
    ]
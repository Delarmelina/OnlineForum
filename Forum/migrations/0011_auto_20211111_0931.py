# Generated by Django 3.2.8 on 2021-11-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0010_rename_filters_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Detail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FilterProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FilterSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Filter',
        ),
    ]

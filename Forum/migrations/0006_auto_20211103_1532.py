# Generated by Django 3.2.8 on 2021-11-03 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_remove_post_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNull',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Forum.usernull'),
        ),
    ]

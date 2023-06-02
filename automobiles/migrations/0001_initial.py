# Generated by Django 4.2 on 2023-05-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=10, verbose_name='Brand')),
                ('model', models.CharField(max_length=10, verbose_name='Model')),
                ('reg_number', models.CharField(max_length=10, verbose_name='Registration Number')),
            ],
        ),
    ]
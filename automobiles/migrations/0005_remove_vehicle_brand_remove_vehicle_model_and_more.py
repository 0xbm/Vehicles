# Generated by Django 4.2 on 2023-06-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobiles', '0004_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='model',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='tech_insp',
            field=models.DateField(verbose_name='Technical Inspection'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='brand',
            field=models.ManyToManyField(blank=True, to='automobiles.brand'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.ManyToManyField(blank=True, to='automobiles.model'),
        ),
    ]

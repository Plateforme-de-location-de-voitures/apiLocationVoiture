# Generated by Django 3.2.5 on 2023-08-12 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marque', '0001_initial'),
        ('modele', '0002_alter_modele_marque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modele',
            name='marque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marque.marque'),
        ),
    ]

# Generated by Django 3.2.5 on 2023-08-12 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0002_auto_20230812_2030'),
        ('users', '0002_alter_personne_role'),
        ('reservation', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='voiture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='voiture.voiture'),
        ),
    ]

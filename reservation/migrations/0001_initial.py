# Generated by Django 3.2.5 on 2023-07-26 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateReservation', models.DateField()),
                ('dateRetour', models.DateField()),
                ('statutReservation', models.BooleanField(default=False)),
            ],
        ),
    ]
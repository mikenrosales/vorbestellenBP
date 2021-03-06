# Generated by Django 3.2.6 on 2022-03-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vorbestellenapp', '0003_alter_reservations_room_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='barangay',
            field=models.CharField(default='Not set', max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='city',
            field=models.CharField(default='Not set', max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='contact',
            field=models.CharField(default='Not set', max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(default='Not set', max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default='Not set', max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.CharField(default='Incomplete', max_length=20),
        ),
    ]

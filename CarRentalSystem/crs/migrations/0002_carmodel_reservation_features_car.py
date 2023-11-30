# Generated by Django 4.2.7 on 2023-11-23 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255, unique=True)),
                ('year', models.CharField(max_length=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('available_from_date', models.DateField(null=True)),
                ('available_to_date', models.DateField(null=True)),
                ('location', models.CharField(choices=[('Dublin', 'Dublin'), ('Cork', 'Cork'), ('Limerick', 'Limerick')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'car_models',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('years_no_claims', models.PositiveIntegerField(blank=True, null=True)),
                ('penalty_point', models.PositiveIntegerField(blank=True, null=True)),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('is_under_25', models.BooleanField()),
                ('is_child_seat', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='crs.carmodel')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='crs.carmodel')),
            ],
            options={
                'db_table': 'features',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('features', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='crs.carmodel')),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_reservations', to='crs.reservation')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
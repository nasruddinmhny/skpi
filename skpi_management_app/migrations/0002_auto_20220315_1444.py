# Generated by Django 3.2.9 on 2022-03-15 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skpi_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='nama',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='programstudi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skpi_management_app.programstudi'),
        ),
    ]
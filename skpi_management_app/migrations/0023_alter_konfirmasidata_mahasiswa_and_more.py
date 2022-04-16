# Generated by Django 4.0.3 on 2022-04-16 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skpi_management_app', '0022_konfirmasidata_created_at_konfirmasidata_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konfirmasidata',
            name='mahasiswa',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='skpi_management_app.mahasiswa'),
        ),
        migrations.AlterField(
            model_name='konfirmasidata',
            name='setuju',
            field=models.CharField(choices=[('SUDAH', 'SUDAH'), ('BELUM', 'BELUM')], max_length=50),
        ),
    ]
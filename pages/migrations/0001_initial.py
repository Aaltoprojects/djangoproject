# Generated by Django 2.2.7 on 2019-12-04 20:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Rakennustyyppi', 'Rakennustyyppi'), ('Rakennusmateriaali', 'Rakennusmateriaali'), ('Palvelu', 'Palvelu'), ('Rakennustoimenpide', 'Rakennustoimenpide'), ('Rakenneosa', 'Rakenneosa')], max_length=200, verbose_name='Filtterikategoria')),
                ('filter_name', models.CharField(max_length=200, verbose_name='Filtteri')),
            ],
            managers=[
                ('filter_db', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200, verbose_name='Projektin nimi')),
                ('destination_name', models.CharField(max_length=200, verbose_name='Kohteen nimi')),
                ('start_date', models.DateField(null=True, verbose_name='Aloituspäivämäärä')),
                ('end_date', models.DateField(null=True, verbose_name='Lopetuspäivämäärä')),
                ('keywords', models.CharField(max_length=200, null=True, verbose_name='Avainsanat')),
                ('project_description', models.CharField(max_length=10000, null=True, verbose_name='Projektin kuvaus')),
                ('documentation_path', models.CharField(max_length=500, null=True, verbose_name='Polku tiedostojen sijaintiin')),
                ('project_manager', models.CharField(max_length=100, null=True, verbose_name='Projektin vetäjä')),
                ('filters', models.ManyToManyField(to='pages.Filter')),
            ],
            managers=[
                ('project_db', django.db.models.manager.Manager()),
            ],
        ),
    ]

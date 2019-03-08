# Generated by Django 2.1.5 on 2019-03-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=30)),
                ('surname', models.CharField(default=None, max_length=30)),
                ('pnumber', models.CharField(default=None, max_length=30)),
                ('email', models.CharField(default=None, max_length=30)),
                ('title', models.CharField(default=None, max_length=30)),
                ('function', models.CharField(default=None, max_length=30)),
                ('siivous', models.IntegerField(default=None)),
                ('tetsaus', models.IntegerField(default=None)),
                ('johtaminen', models.IntegerField(default=None)),
            ],
        ),
    ]

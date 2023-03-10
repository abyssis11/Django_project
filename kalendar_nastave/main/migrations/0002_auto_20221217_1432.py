# Generated by Django 3.2.12 on 2022-12-17 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Racunalo',
            fields=[
                ('broj_racunala', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('marka', models.CharField(max_length=10)),
                ('tip', models.CharField(max_length=20)),
                ('operacijski_sustav', models.CharField(max_length=20)),
                ('mreza', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Novi',
        ),
        migrations.AddField(
            model_name='prostorija',
            name='glavno_racunalo',
            field=models.OneToOneField(default=404, on_delete=django.db.models.deletion.CASCADE, to='main.racunalo'),
        ),
    ]

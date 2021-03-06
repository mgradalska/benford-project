# Generated by Django 3.1.1 on 2020-09-13 14:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='datasets')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('graph', models.ImageField(null=True, upload_to='images')),
                ('distribution_match', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FirstNumberStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('percentage', models.DecimalField(decimal_places=4, max_digits=5)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='benford_analyzer.dataset')),
            ],
        ),
    ]

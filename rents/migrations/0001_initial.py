# Generated by Django 5.0.6 on 2024-07-05 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipments', '0001_initial'),
        ('members', '0003_member_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(null=True)),
                ('fee', models.IntegerField(null=True)),
                ('equipment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipments.equipment')),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]

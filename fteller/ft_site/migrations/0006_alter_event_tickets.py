# Generated by Django 4.1.5 on 2023-01-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft_site', '0005_alter_event_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tickets',
            field=models.CharField(blank=True, max_length=120, verbose_name='Vstupenky'),
        ),
    ]

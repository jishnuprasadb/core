# Generated by Django 4.0.2 on 2023-04-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0030_events_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

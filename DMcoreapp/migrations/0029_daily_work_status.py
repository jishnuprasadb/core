# Generated by Django 4.0.2 on 2023-04-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0028_smo_post_executive'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_work',
            name='status',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]

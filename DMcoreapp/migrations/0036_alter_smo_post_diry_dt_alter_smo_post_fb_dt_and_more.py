# Generated by Django 4.0.2 on 2023-05-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0035_alter_addi_smo_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smo_post',
            name='diry_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='fb_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='insta_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='link_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='pin_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='qra_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='sbms_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='tumb_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='tw_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smo_post',
            name='yt_dt',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0003_alter_celulares_id_alter_heladeras_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='celulares',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='celulares'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-30 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0005_heladeras_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='televisores',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='televisores'),
        ),
    ]
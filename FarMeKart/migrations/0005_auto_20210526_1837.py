# Generated by Django 3.2.1 on 2021-05-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0004_vegpro_market_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorders',
            name='cancel',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]

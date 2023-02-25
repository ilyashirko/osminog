# Generated by Django 4.1.7 on 2023-02-25 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_client_options_order_estimated_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientsubscription',
            options={'verbose_name': 'подписка клиента', 'verbose_name_plural': 'подписки клиентов'},
        ),
        migrations.AddField(
            model_name='clientsubscription',
            name='payment_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='salary',
            field=models.IntegerField(default=300, validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость работ'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость подписки'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='Название тарифа'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-02-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='finished_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Заказ выполнен'),
        ),
    ]
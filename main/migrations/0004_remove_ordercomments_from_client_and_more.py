# Generated by Django 4.1.7 on 2023-02-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_order_complaint_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercomments',
            name='from_client',
        ),
        migrations.RemoveField(
            model_name='ordercomments',
            name='from_contractor',
        ),
        migrations.AddField(
            model_name='ordercomments',
            name='author',
            field=models.CharField(blank=True, choices=[('client', 'Клиент'), ('contactor', 'Подрядчик'), ('owner', 'Администратор'), ('manager', 'Менеджер')], max_length=10, null=True, verbose_name='Автор комментария'),
        ),
    ]
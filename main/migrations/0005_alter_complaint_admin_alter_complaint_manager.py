# Generated by Django 4.1.7 on 2023-02-26 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_ordercomments_from_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to='main.owner', verbose_name='админ'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to='main.manager', verbose_name='менеджер'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-25 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_person_options_alter_client_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='main.person', verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='contractors', to='main.person', verbose_name='Подрядчик'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='managers', to='main.person', verbose_name='менеджер'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='owners', to='main.person', verbose_name='Администратор'),
        ),
    ]
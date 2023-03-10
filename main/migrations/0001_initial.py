# Generated by Django 4.1.7 on 2023-02-25 16:48

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='ClientSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='Старт подписки')),
                ('payment_id', models.CharField(blank=True, max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='main.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'подписка клиента',
                'verbose_name_plural': 'подписки клиентов',
            },
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='исполнитель утвержден')),
                ('comment', models.TextField(blank=True, verbose_name='заявка на утверждение')),
            ],
            options={
                'verbose_name': 'подрядчик',
                'verbose_name_plural': 'подрядчики',
            },
        ),
        migrations.CreateModel(
            name='ExampleOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст заявки')),
            ],
            options={
                'verbose_name': 'пример заявки',
                'verbose_name_plural': 'примеры заявок',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость работ')),
                ('description', models.TextField(verbose_name='Текст заявки')),
                ('declined', models.BooleanField(default=False, verbose_name='Заявка отклонена')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Заказ создан')),
                ('take_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Взят в работу')),
                ('estimated_time', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Срок выполнения заказа')),
                ('finished_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Заказ выполнен')),
                ('contractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='main.contractor', verbose_name='подрядчик')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='main.clientsubscription', verbose_name='Подписка')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Номер телефона')),
                ('telegram_id', models.SmallIntegerField(unique=True, verbose_name='Телеграм ID')),
            ],
            options={
                'verbose_name': 'контакты пользователя',
                'verbose_name_plural': 'контакты пользователей',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Название тарифа')),
                ('orders_limit', models.IntegerField(verbose_name='Лимит заявок в месяц')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость подписки')),
                ('validity', models.DurationField(default=datetime.timedelta(days=30), verbose_name='Срок действия')),
                ('answer_delay', models.DurationField(verbose_name='Время ответа на заявку')),
                ('contractor_contacts_availability', models.BooleanField(default=False, verbose_name='Возможность видеть контакты подрядчика')),
                ('personal_contractor_available', models.BooleanField(default=False, verbose_name='Закрепить за собой подрядчика')),
            ],
            options={
                'verbose_name': 'тариф',
                'verbose_name_plural': 'тарифы',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='owners', to='main.person', verbose_name='Администратор')),
            ],
            options={
                'verbose_name': 'администратор',
                'verbose_name_plural': 'администратор',
            },
        ),
        migrations.CreateModel(
            name='OrderComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_client', models.BooleanField(default=False, verbose_name='Комментарий клиента')),
                ('from_contractor', models.BooleanField(default=False, verbose_name='Комментарий клиента')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='main.order', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='managers', to='main.person', verbose_name='менеджер')),
            ],
            options={
                'verbose_name': 'менеджер',
                'verbose_name_plural': 'менеджеры',
            },
        ),
        migrations.AddField(
            model_name='contractor',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='contractors', to='main.person', verbose_name='Подрядчик'),
        ),
        migrations.AddField(
            model_name='clientsubscription',
            name='contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='main.contractor', verbose_name='Подрядчик'),
        ),
        migrations.AddField(
            model_name='clientsubscription',
            name='tariff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='main.tariff', verbose_name='Тариф'),
        ),
        migrations.AddField(
            model_name='client',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='main.person', verbose_name='Клиент'),
        ),
    ]

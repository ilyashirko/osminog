from django.db import models
from django.utils.timezone import now, timedelta
from phonenumber_field.modelfields import PhoneNumberField


def end_period():
    return now() + timedelta(days=30)


class Person(models.Model):
    ROLE = (
        ('client', 'Клиент'),
        ('contractor', 'Подрядчик'),
        ('admin', 'Заказчик проекта'),
        ('manager', 'Менеджер')
    )
    telegram_id = models.IntegerField('Телеграм user_id')
    role = models.CharField(verbose_name='Тип пользователя', max_length=10, choices=ROLE)
    phone = PhoneNumberField(verbose_name='Номер телефона', db_index=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'Роль: {self.role} Телеграм id: {self.telegram_id}'


class Order(models.Model):
    client = models.ForeignKey(
        Person,
        related_name='client_orders',
        verbose_name='клиент',
        on_delete=models.PROTECT
    )
    contractor = models.ForeignKey(
        Person,
        related_name='contractor_orders',
        verbose_name='подрядчик',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    text = models.CharField('Текст заявки', max_length=200)
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Заказ создан', auto_now_add=True, db_index=True)
    finished_at = models.DateTimeField('Заказ выполнен', blank=True, db_index=True)
    is_payed = models.BooleanField('Заказ оплачен', default=False)
    is_closed = models.BooleanField('Заказ закрыт', default=False)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.client} {self.text} -> {self.contractor}'


class Tariff(models.Model):
    name = models.CharField('Название тарифа', max_length=20)
    limit_orders = models.IntegerField('Лимит заявок в месяц')
    limit_time_answer = models.IntegerField('Время ответа на заявку в часах')
    can_see_contractor = models.BooleanField('Возможность видеть контакты подрядчика', default=False)
    can_attach_contractor = models.BooleanField('Закрепить за собой подрядчика', default=False)

    class Meta:
        verbose_name = 'тариф'
        verbose_name_plural = 'тарифы'

    def __str__(self):
        return f'"{self.name}" до {self.limit_orders} заявок. Отклик в течении {self.limit_time_answer} часов'


class ClientContract(models.Model):
    client = models.ForeignKey(
        Person,
        verbose_name='договор',
        related_name='client_contracts',
        on_delete=models.CASCADE
    )
    tariff = models.ForeignKey(
        Tariff,
        verbose_name='тариф',
        on_delete=models.SET_NULL,
        null=True
    )
    orders_limit_to = models.DateTimeField('конец периода', default=end_period)
    orders_left = models.IntegerField('остаток заявок')
    is_working = models.BooleanField('действующий', default=True)
    attach_contactor = models.ForeignKey(
        Person,
        verbose_name='закрепленный подрядчик',
        related_name='contractor_contracts',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'договор клиента'
        verbose_name_plural = 'договора клиентов'

    def __str__(self):
        return f'{self.client}, {self.tariff} Остаток заявок: {self.orders_left}'


class ContractorContract(models.Model):
    contractor = models.ForeignKey(
        Person,
        verbose_name='договор подрядчика',
        on_delete=models.CASCADE
    )
    order_price = models.IntegerField('Стоимость заказа', blank=True)

    class Meta:
        verbose_name = 'договор подрядчика'
        verbose_name_plural = 'договора подрядчиков'

    def __str__(self):
        return f'{self.contractor}, стоимость заявки: {self.order_price}'


class ExampleOrder(models.Model):
    text = models.CharField('Текст заявки', max_length=200)

    class Meta:
        verbose_name = 'пример заявки'
        verbose_name_plural = 'примеры заявок'

    def __str__(self):
        return self.text
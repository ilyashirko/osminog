# Просьба созранять алфавитный порядок

BACK_TO_CLIENT_MAIN = {'text': 'На главную', 'callback_data': 'client_main'}

CANCEL = {'text': "Я передумал", 'callback_data': 'cancel'}

CHECK_ACCESS_CALLBACK = 'check_access'

I_AM_OWNER = {'text': 'Я владелец', 'callback_data': f'{CHECK_ACCESS_CALLBACK}:::owner'}

I_AM_CONTACTOR = {'text': 'Я подрядчик', 'callback_data': f'{CHECK_ACCESS_CALLBACK}:::contractor'}

I_AM_MANAGER = {'text': 'Я менеджер', 'callback_data': f'{CHECK_ACCESS_CALLBACK}:::manager'}

I_AM_CLIENT = {'text': 'Я заказчик', 'callback_data': f'{CHECK_ACCESS_CALLBACK}:::client'}

CONTRACTOR_CONTACTS = {'text': "Показать контакты подрядчика", "callback_data": 'send_contractor_contacts'}

CONTRACTOR_CURRENT_ORDERS = {'text': 'Посмотреть актуальные заказы', 'callback_data': 'contractor_current_orders'}

CLIENT_CURRENT_ORDERS = {'text': 'Мои текущие заказы', 'callback_data': 'client_current_orders'}

CLIENT_CURRENT_TARIFF = {'text': 'Мой тариф', 'callback_data': 'client_current_tariff'}

CREATE_SUBSCRIPTION = {'text': 'Оформить подписку', 'callback_data': 'create_subscription'}

FILL_CONTRACTOR_FORM = {'text': 'Заполнить анкету', 'callback_data': 'fill_contractor_form'}

NEW_CONTRACTOR = {'text': 'Стать подрядчиком', 'callback_data': 'new_contractor'}

NEW_CLIENT = {'text': 'Стать клиентом', 'callback_data': 'new_client'}

NEW_REQUEST = {'text': 'Отправить заявку', 'callback_data': 'new_request'}

ORDER = {'text': 'Заказ', 'callback_data': 'show_order'}

ORDER_COMMENT = {'text': 'Отправить уточнение', 'callback_data': 'new_order_comment'}

ORDER_COMPLAINT = {'text': 'Есть претензия', 'callback_data': 'complaint'}

PHONENUMBER_REQUEST = 'Поделиться номером'
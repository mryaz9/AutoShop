LEXICON: dict[str, str] = {
    '/start': '<b>Приветствуем!</b>\n\nЧтобы посмотреть список доступных '
              'команд - набери /help',
    '/help': '<b>Это бот</b>\n\nДоступные команды:\n\n',
    'assortment': 'Ниже представлен ассортимент',
    'profile': 'Профиль',
    '️orders': 'Заказы',
    'information': 'Информация',
    'to_main': '🏚',
    'back': '<--',
}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Начало работы',
    '/help': 'Справка по работе бота'
}

LEXICON_BUTTON_MAIN: dict[str, str] = {
    'assortment': '⚡Ассортимент',
    'profile': '💳Профиль',
    '️orders': '⚙️Заказы',
    'information': 'ℹ️Информация'
}

LEXICON_BUTTON_ADMIN: dict[str, str] = {
    'add_assortment': 'Добавить ассортимент',
    'del_assortment': 'Удалить ассортимент',
    'see_admin': 'Администраторы'
}

LEXICON_NAME_CATALOG: dict[str, str] = {
    'services': 'Услуги',
    'product': 'Товары'
}

LEXICON_FSM_SHOP: dict[str, str] = {
    'done': 'Товар успешно создан\nВсе правильно?',
    'done_yes': 'Товар добавлен в магазин',
    'done_no': 'Товар удален',
    'cancel': 'Отмена',
    'unknown': 'Неверный ввод\nЧто бы отменить создание используйте команду /cancel',

    'catalog': 'Каталог:',
    'name': 'Наименование:',
    'price': 'Цена:',
    'time_action': 'Время использования (в днях):',
    'description': 'Описание:'
}

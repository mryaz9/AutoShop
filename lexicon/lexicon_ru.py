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

LEXICON_ADMIN: dict[str, str] = {
    'in_admin': 'Режим администратора',
    'exit_admin': 'Выход из режима администратора'
}

LEXICON_ADMIN_INFO: dict[str, str] = {
    'startup': 'Бот запущен!',
    'shutdown': 'Бот остановлен!'
}

LEXICON_INLINE_MENU: dict[str, str] = {
    'category_code': 'Каталог:',
    'subcategory': 'Подкаталог:',
    'name': 'Наименование:',
    'card': 'Товар'
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
    'see_admin': 'Администраторы',
    'back': 'Выйти'
}

LEXICON_FSM_SHOP: dict[str, str] = {
    'done': 'Товар успешно создан\nВсе правильно?',
    'done_yes': 'Товар добавлен в магазин',
    'done_no': 'Товар удален',
    'cancel': 'Отмена',
    'unknown': 'Неверный ввод\nЧто бы отменить создание используйте команду /cancel',
    'add_new_category': "Добавить",

    'category_code': 'Каталог:',
    'subcategory': 'Подкаталог:',
    'name': 'Наименование:',
    'price': 'Цена:',
    'photo': 'Фото:',
    'time_action': 'Время использования (в днях):',
    'description': 'Описание:'
}

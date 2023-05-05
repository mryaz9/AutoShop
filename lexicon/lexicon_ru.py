LEXICON_MAIN: dict[str, str] = {
    'start': '<b>Приветствуем!</b>\n\nЧтобы посмотреть список доступных '
             'команд - набери /help',
    '/help': '<b>Это бот</b>\n\nДоступные команды:\n\n',
    'assortment': 'Ниже представлен ассортимент',
    'profile': 'Профиль',
    '️orders': 'Заказы',
    'information': 'Информация',
    'to_main': '🏚',
    'back': '<--',
    'exit': 'Выход',
    'buy': 'Купить'
}
LEXICON_ADMIN: dict[str, str] = {
    'in_admin': 'Режим администратора',
    'out_admin': 'Выход из режима администратора'
}

LEXICON_ADMIN_INFO: dict[str, str] = {
    'startup': 'Бот запущен!',
    'shutdown': 'Бот остановлен!'
}

LEXICON_INLINE_MENU: dict[str, str] = {
    'category': 'Каталог:',
    'subcategory': 'Подкаталог:',
    'name': 'Наименование:',
    'card': 'Товар',
    'item': '{product.name}\n{product.price}руб.\nОписание: {product.description}'
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
    'add_assortment': 'Добавить товар',
    'show_assortment': 'Скрыть/показать товар',
    'del_assortment': 'Удалить ассортимент',
    'see_admin': 'Администраторы',
    'exit': 'Выход'
}

LEXICON_FSM_SHOP: dict[str, str] = {
    'start': 'Начало добавления нового товара',
    'done_yes': 'Товар добавлен в магазин',
    'done_no': 'Товар удален',
    'cancel': 'Отмена',
    'unknown': 'Неверный ввод\nОт вас ожидается: {state}\nЧто бы отменить создание используйте команду /cancel',
    'add_new_category': "Добавить",
    'error': 'Произошла ошибка, попробуйте еще раз\n{error}',

    'category_code': 'Каталог:',
    'subcategory_code': 'Подкаталог:',

    'new_category_code': 'Укажите название каталога (обязательно на английском)(для работы программы)',
    'new_category_name': 'Укажите название каталога (которое отображается)',
    'new_subcategory_code': 'Укажите название подкаталога (обязательно на английском)(для работы программы)',
    'new_subcategory_name': 'Укажите название подкаталога (которое отображается)',

    'name': 'Наименование:',
    'amount': 'Количество',
    'price': 'Цена:',
    'photo': 'Фото:',
    'time_action': 'Время использования (в днях):',
    'description': 'Описание:',

    'done_1': 'Каталог: {category_id}\nПодкаталог: {subcategory_id}',
    'done_2': 'Название: {name}\nКол-во: {amount}\n{price} руб.\nВремя действия: {time_action}\nОписание: {description}'
}

LEXICON_MAIN: dict[str, str] = {
    'start': 'Вас приветствует команда TGC!\n'
             'Добро пожаловать, {username}!',
    'assortment': '🛍️ Каталог товаров',
    'profile': '💳 Профиль',
    '️orders': '⚙️ Заказы',
    'information': 'ℹ️ Информация',
    'admin': '👁‍🗨 Меню админа',
}

LEXICON_ASSORTIMENT: dict[str, str] = {
    'categories': '"Каталог товаров" 🛍️',
    'error_categories': 'Сначала выберете категорию',

    'subcategories': '"Подкаталог товаров" 🛍️',
    'not_subcategories': 'Нет подкатегорий',
    'error_subcategories': 'Сначала выберете подкатегорию',

    'items': '"Товары" 🛍️',
    'not_items': 'Нет товаров',
    'error_items': 'Сначала выберете продукт',

    'card': '🎁 Покупка товара:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
            '🏷 Название: {product.title}\n'
            '💵 Стоимость: {product.price}руб.\n'
            '📜 Описание: {product.description}\n',

    # У product есть атрибуты:
    # amount, price, name, id, show, subcategory_id,
    # admin_id_add, description, photo, time_action

    'buy_product': '"Купить" 💰',

    'buy_product_window': '✅ Вы выбрали: {product.title}\n'  # Тут так же как выше
                          'Сколько вы хотите купить?',

    'error_input_amount': 'Введите число',
    'error_not_items': 'Недостаточно товаров',

    'buy_product_amount': 'Имеется {amount}шт.',  # Этот текст отображается только если имеется количество

    'accept_buy_item': 'Вы хотите купить: {product.title}\n'
                       'За {total_amount}руб.\n\n'
                       'Все верно?',

    'accept_buy_item_amount': 'Вы выбрали {amount_user}шт.\n',

    'confirm_buy': 'Да',
    'error_unknown_username': 'Создайте username',
    'error_not_money': 'Недостаточно средств',

    'successful_buy_item': '✅Вы купили {title}\n'
                           'Спасибо за покупку!',

    'send_admin_buy': 'Товар: {title}\n'
                       'Кол-во: {amount_user}\n'
                       'Покупатель: @{username}\n',

    'back_select_categories': 'Изменить категорию',
    'back_select_subcategories': 'Изменить подкатегорию',
    'back_select_items': 'Изменить товар',
    'back_items_info': 'Вернуться к описанию товара',
    'back_items_names': 'Выбрать другой продукт',
    'back_items_amount': 'Изменить количество',

    'to_menu': 'В основное меню'
}

LEXICON_PROFILE: dict[str, str] = {
    'to_menu': 'В основное меню'
}

LEXICON_PAYMENT: dict[str, str] = {
    'payment_menu': 'Выберите способ оплаты',

    'qiwi': 'Qiwi',
    'crypto': 'Crypto_bot',
    'admin': 'Пополнить баланс (Для админов)',

    'input_amount': 'Введите сумму',
    'select_assets': 'Выберите валюту',

    'back_input_amount': 'Изменить сумму',
    'back_select_assets': 'Изменить валюту',

    'to_payment_menu': 'В меню выбора оплаты',
    'to_menu': 'В основное меню',
}


LEXICON_ADMIN_MENU: dict[str, str] = {
    'admin_menu': 'Меню администратора',
    'to_menu': 'В основное меню',
}

LEXICON_ADMIN: dict[str, str] = {
    'admin_menu': 'Администраторы',
    'add_admin': 'Добавить админа',
    'view_admin': 'Список админов',
    'select_admin': 'При нажатии администратор удаляется',
    'input_id_admin': 'Введите id',
    'successful_add_admin': 'Администратор {admin_id} добавлен успешно!',
    'successful_del_admin': 'Администратор {admin_id} удален успешно!',

    'to_menu': 'В основное меню',
    'to_admin_menu': 'В меню администратора'
}

LEXICON_CATEGORIES: dict[str, str] = {
    'categories_menu': 'Категории/подкатегории',

    'input_name_categories': 'Добавить категорию',
    'del_categories': 'Удалить категорию',
    'del_categories_confirm': 'Вы уверены? При удалении потеряются все подкатегории и товары',
    'back_del_categories_confirm': 'Изменить категорию',
    'successful_del_categories': 'Категория удалена успешно',

    'add_subcategories': 'Добавить подкатегорию',
    'del_subcategories': 'Удалить подкатегорию',
    'del_subcategories_confirm': 'Вы уверены? При удалении потеряются все товары',
    'back_del_subcategories_confirm': 'Изменить подкатегорию',
    'successful_del_subcategories': 'Подкатегория удалена успешно',

    'select_category': 'Выберите категорию',
    'select_subcategory': 'Выберите подкатегорию',

    'input_new_category': 'Введите название новой категории',
    'input_new_subcategory': 'Введите название новой подкатегории',

    'input_photo': 'Загрузите фото',

    'add_categories_confirm': '{dialog_data[title]}\nВсе верно?',
    'back_add_categories_confirm': 'Изменить фото',
    'successful_add_category': 'Категория добавлена успешно!',

    'add_subcategories_confirm': '{dialog_data[title]}\nВсе верно?',
    'back_add_subcategories_confirm': 'Изменить фото',
    'successful_add_subcategory': 'Подкатегория добавлена успешно!',

    'error_db': 'Произошла ошибка при работе с бд',

    'to_menu': 'В основное меню',
    'to_category_menu': 'В меню категорий'
}

LEXICON_ITEM: dict[str, str] = {
    'item_menu': 'Товары',

    'add_item': 'Добавить товар',
    'add_files': 'Добавить файлы',
    'add_files_confirm': 'Добавить файлы?',
    'del_item': 'Удалить товар',

    'del_item_confirm': 'Удалить товар?',
    'successful_del_item': 'Товар удален успешно',

    'select_category': 'Выберите категорию',

    'select_subcategory': 'Выберите подкатегорию',

    'select_item': 'Выберите продукт',


    'input_name': 'Введите имя',
    'back_input_name': 'Изменить подкатегорию',

    'input_amount': 'Загрузите документы',
    'back_input_amount': 'Изменить имя',

    'input_photo': 'Загрузите фото',
    'back_input_photo': 'Изменить количество',

    'input_price': 'Введите цену',
    'back_input_price': 'Изменить фото',

    'input_description': 'Введите описание',
    'back_input_description': 'Изменить цену',

    'back_input_confirm': 'Изменить описание',

    'confirm': 'Все правильно?\n'
               'Каталог: {category}\n'
               'Подкаталог: {subcategory}\n'
               'Название: {title}\n'
               'Кол-во: {amount}\n'
               'Цена {price} руб.\n'
               'Описание: {description}',

    'done': 'Товар добавлен в магазин',

    'to_menu': 'В основное меню',
    'to_item_menu': 'В меню товара'
}

LEXICON_MAILING: dict[str, str] = {
    'item_menu': 'Рассылка',
    'create_mailing': 'Создать рассылку',
    'successful_add_mailing': 'Сообщение добавлено успешно!',

    'to_menu': 'В основное меню',
    'to_mailing_menu': 'В меню рассылки'

}

LEXICON_ADMIN_INFO: dict[str, str] = {
    'startup': 'Бот запущен!',
    'shutdown': 'Бот остановлен!'
}

LEXICON_CHANGE_MENU: dict[str, str] = {
    'change_menu': 'Изменить меню',
    'main_menu': 'Фото основного меню',
    'catalog': 'Фото каталога',
    'order': 'Фото заказов',
    'profile': 'Фото профиля',
    'info': 'Фото информации',
    'info_about': 'Текст о нас',
    'back': "⬅️ Назад ↩️",
    'to_menu': "🏠 Меню 🏠"
}

BUTTON_MENU: dict[str, str] = {
    'back': "⬅️ Назад ↩️",
    'to_menu': "🏠 Меню 🏠"
}

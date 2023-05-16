LEXICON_MAIN: dict[str, str] = {
    'start': 'Вас приветствует команда TGC!\n'
             'Добро пожаловать!',
    'assortment': '⚡Ассортимент',
    'profile': '💳Профиль',
    '️orders': '⚙️Заказы',
    'admin': 'ℹ️Меню админа',
}

LEXICON_ASSORTIMENT: dict[str, str] = {
    'categories': 'Каталог:',
    'error_categories': 'Сначала выберете категорию',

    'subcategories': 'Подкаталог:',
    'not_subcategories': 'Нет подкатегорий',
    'error_subcategories': 'Сначала выберете подкатегорию',

    'items': 'Товары:',
    'not_items': 'Нет товаров',
    'error_items': 'Сначала выберете продукт',

    'card': 'Товар:\n'
            '{product.name}\n'
            '{product.price}руб.\n',

    'description': 'Описание: {product.description}\n',
    # У product есть атрибуты:
    # amount, price, name, id, show, subcategory_id,
    # admin_id_add, description, photo, time_action

    'buy_product': 'Купить',

    'buy_product_window': 'Вы выбрали: {product.name}\n'  # Тут так же как выше
                          'Сколько вы хотите купить?',

    'error_input_amount': 'Введите число',
    'error_not_items': 'Недостаточно товаров',

    'buy_product_amount': 'Имеется {product.amount}шт.',  # Этот текст отображается только если имеется количество

    'accept_buy_item': 'Вы хотите купить {product.name}\n'
                       'За {total_amount}руб.\n'
                       'Вы уверены?',

    'accept_buy_item_amount': 'Вы выбрали {amount_user} шт\n',

    'confirm_buy': 'Да',
    'error_unknown_username': 'Создайте username',
    'error_not_money': 'Недостаточно средств',

    'successful_buy_item': 'Вы купили {amount}шт. {product_info.name}',

    'send_admin_buy': 'Номер заказа: #{purchases_get.id}\n'
                       'Товар: {product_info.name}\n'
                       'Кол-во: {purchases_get.amount}\n'
                       'Имя: {user.full_name}\n'
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
    'admin_menu': 'Редактирование администраторов',
    'add_admin': 'Добавить админа',
    'input_id_admin': 'Введите id',
    'successful_add_admin': 'Администратор {admin_id} добавлен успешно!',
    'successful_del_admin': 'Администратор {admin_id} удален успешно!',

    'to_menu': 'В основное меню',
    'to_admin_menu': 'В меню администратора'
}

LEXICON_CATEGORIES: dict[str, str] = {
    'categories_menu': 'Редактирование категорий',
    'add_categories': 'Добавить категорию',
    'add_subcategories': 'Добавить подкатегорию',
    'select_category': 'Выберите категорию',

    'input_new_category': 'Введите название новой категории',
    'input_new_subcategory': 'Введите название новой подкатегории',

    'successful_add_category': 'Категория {category} добавлена успешно!',
    'successful_add_subcategory': 'Подкатегория {subcategory} добавлена успешно!',

    'to_menu': 'В основное меню',
    'to_category_menu': 'В меню категорий'
}

LEXICON_ITEM: dict[str, str] = {
    'item_menu': 'Редактирование товара',
    'add_item': 'Добавить товар',

    'hide_item': 'Скрыть или показать товары',
    'hide_on': 'Товар показывается',
    'hide_off': 'Товар скрыт',

    'select_category': 'Выберите категорию',

    'select_subcategory': 'Выберите подкатегорию',

    'input_name': 'Введите имя',
    'back_input_name': 'Изменить подкатегорию',

    'input_amount': 'Введите количество',
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
               'Название: {name}\n'
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
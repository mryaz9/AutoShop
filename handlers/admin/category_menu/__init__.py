from aiogram_dialog import Dialog

from handlers.admin.category_menu.window import menu_window


def category_menu_dialogs():
    return [
        Dialog(
            menu_window(),

            input_name_category_window(),
            photo_categories_window(),
            add_categories_confirm_window(),

            del_categories_confirm_window(),
        ),
    ]

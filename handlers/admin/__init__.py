from aiogram_dialog import Dialog

from handlers.admin.window import menu, add_item, add_categories, mailing
from handlers.admin.window import add_admin


def admin_dialogs():
    return [
        Dialog(
            menu.admin_menu_window(),
        ),
        Dialog(
            add_item.menu_window(),
            add_item.hide_item_window(),

            add_item.categories_window(),
            add_item.subcategories_window(),
            add_item.name_window(),
            add_item.amount_window(),
            add_item.photo_window(),
            add_item.price_window(),
            add_item.description_window(),
            add_item.confirm_window(),
        ),
        Dialog(
            add_categories.menu_window(),
            add_categories.select_categories_window(),
            add_categories.add_categories_window(),
            add_categories.add_subcategories_window(),
        ),
        Dialog(
            add_admin.menu_window(),
            add_admin.add_admin_window(),
        ),
        Dialog(
            mailing.menu_window(),
            mailing.create_mailing_window(),
        )
    ]

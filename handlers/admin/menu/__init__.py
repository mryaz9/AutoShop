from aiogram_dialog import Dialog

from handlers.admin.admin_menu import window, admin_menu_dialogs
from handlers.admin.change_menu import change_menu_dialogs


def admin_dialogs():
    return [
        Dialog(
            menu.admin_menu_window(),
        ),
        Dialog(
            add_item.menu_window(),
            add_item.add_files_window(),
            add_item.add_files_confirm_window(),

            add_item.del_item_confirm_window(),

            add_item.categories_window(),
            add_item.subcategories_window(),
            add_item.items_window(),
            add_item.name_window(),
            add_item.amount_window(),
            add_item.photo_window(),
            add_item.price_window(),
            add_item.description_window(),
            add_item.confirm_window(),
        ),
        Dialog(


            add_categories.input_name_subcategory_window(),
            add_categories.photo_subcategories_window(),
            add_categories.add_subcategories_confirm_window(),

            add_categories.del_subcategories_confirm_window()
        ),
        admin_menu_dialogs(),
        change_menu_dialogs(),
        Dialog(
            mailing.menu_window(),
            mailing.create_mailing_window(),
        )
    ]

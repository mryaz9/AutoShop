from aiogram_dialog import Dialog

from dialogs.admin.window import menu, add_product


def admin_dialogs():
    return [
        Dialog(
            menu.admin_menu_window(),
        ),
        Dialog(
            add_product.categories_window(),
            add_product.subcategories_window(),
            add_product.name_window(),
            add_product.amount_window(),
            add_product.photo_window(),
            add_product.price_window(),
            add_product.time_action_window(),
            add_product.description_window(),
            add_product.confirm_window(),
        )
    ]

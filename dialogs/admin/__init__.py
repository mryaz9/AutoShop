from aiogram_dialog import Dialog

from dialogs.admin import windows


def admin_dialogs():
    return [
        Dialog(
            windows.admin_menu_window(),
        ),
        Dialog(
            windows.categories_window(),
            windows.subcategories_window(),
            windows.name_window(),
            windows.amount_window(),
            windows.photo_window(),
            windows.price_window(),
            windows.time_action_window(),
            windows.description_window(),
            windows.confirm_window(),
        )
    ]

from aiogram_dialog import Dialog

from dialogs.admin import windows


def admin_dialogs():
    return [
        Dialog(
            windows.categories_window(),
            windows.subcategories_window(),
        ),
        Dialog(
            windows.product_window(),
        )
    ]
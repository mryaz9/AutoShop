from aiogram_dialog import Dialog

from dialogs.assortiment import windows


def bot_menu_dialogs():
    return [
        Dialog(
            windows.categories_window(),
            windows.subcategories_window(),
            windows.product_window(),
            windows.product_info_window(),
            on_process_result=windows.on_process_result
        ),
        Dialog(
            windows.buy_product_window(),
            windows.confirm_buy_window()
        ),
    ]

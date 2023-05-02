from aiogram_dialog import Dialog

from dialogs.bot_main_menu import windows


def bot_menu_dialogs():
    return [
        Dialog(
            windows.categories_window(),
            windows.subcategory_window(),
            windows.product_window(),
            windows.produst_info(),
            on_process_result=windows.on_process_result()
        ),
        Dialog(
            windows.buy_product_window(),
            windows.confirm_buy_product_window()
        )
    ]

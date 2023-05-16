from aiogram_dialog import Dialog

from handlers.menu import windows


def main_menu_dialogs():
    return [
        Dialog(
            windows.main_menu_window(),
        )
    ]

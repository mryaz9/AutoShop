from aiogram_dialog import Dialog

from dialogs.main_menu import windows


def main_menu_dialogs():
    return [
        Dialog(
            windows.main_menu_window(),
        )
    ]

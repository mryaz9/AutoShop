from aiogram_dialog import Dialog

from handlers.menu import main_windows, info_window


def main_menu_dialogs():
    return [
        Dialog(
            main_windows.main_menu_window(),
        ),
        Dialog(
            info_window.info_window(),
        )
    ]

from aiogram_dialog import Dialog

from bot_tgc.handlers.menu import info_window
from bot_tgc.handlers.menu import main_windows


def main_menu_dialogs():
    return [
        Dialog(
            main_windows.main_menu_window(),
        ),
        Dialog(
            info_window.info_window(),
        )
    ]

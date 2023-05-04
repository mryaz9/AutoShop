from aiogram_dialog import Dialog

from dialogs.admin import windows


def admin_dialogs():
    return [
        Dialog(
            windows.select_utils_window(),

        )
    ]
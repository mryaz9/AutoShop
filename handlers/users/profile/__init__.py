from aiogram_dialog import Dialog

from handlers.users.profile import windows


def profile_dialogs():
    return [
        Dialog(
            windows.profile_window(),
        ),
        Dialog(
            windows.orders_window(),

        ),
    ]

from aiogram_dialog import Dialog

from bot_tgc.handlers.users.profile import windows


def profile_dialogs():
    return [
        Dialog(
            windows.profile_window(),
        ),
    ]

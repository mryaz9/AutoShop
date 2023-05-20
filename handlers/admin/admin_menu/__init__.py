from aiogram_dialog import Dialog

from handlers.admin.admin_menu.window import menu_window, add_admin_window, view_admin_window


def admin_menu_dialogs():
    return [
        Dialog(
            menu_window(),
            add_admin_window(),
            view_admin_window()
        ),
    ]

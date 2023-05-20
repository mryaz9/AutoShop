from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from database.command.main_menu import create_menu
from schemas.admin import MenuModel


async def confirm_change_menu(callback: CallbackQuery, btn: Button, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()

    menu = MenuModel(**ctx.widget_data)
    await create_menu(session, menu)

    await manager.done()

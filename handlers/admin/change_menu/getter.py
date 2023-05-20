from aiogram_dialog import DialogManager


async def change_menu_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    ctx = dialog_manager.current_context()
    data = ctx.widget_data
    return {"change_menu": data.keys()}

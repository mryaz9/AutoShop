from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot_tgc.database.models import MainMenu
from bot_tgc.schemas.admin import MenuModel


async def create_menu(
        session: AsyncSession,
        menu_obj: MenuModel,
) -> None:
    """
    Create the Item instance, shops are list of (shop_id, quantity), photos are list of (file_id)
    """

    old_menu = await get_menu(session)
    if old_menu is not None:
        menu = old_menu
    else:
        menu = MainMenu()

    if menu_obj.main_menu:
        menu.main_menu = menu_obj.main_menu

    if menu_obj.catalog:
        menu.catalog = menu_obj.catalog

    if menu_obj.order:
        menu.order = menu_obj.order

    if menu_obj.profile:
        menu.profile = menu_obj.profile

    if menu_obj.info:
        menu.info = menu_obj.info

    if menu_obj.info_about:
        menu.info_about = menu_obj.info_about

    session.add(menu)

    await session.commit()


async def get_menu(session: AsyncSession) -> MainMenu:
    q = select(MainMenu)

    res = await session.execute(q)

    return res.scalar()

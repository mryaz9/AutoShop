from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Cancel, Group, Url
from aiogram_dialog.widgets.text import Const

from bot_tgc.dictionary.dictionary_ru import LEXICON_ADMIN_MENU, LEXICON_ADMIN, LEXICON_CATEGORIES, LEXICON_ITEM, \
    LEXICON_MAILING, LEXICON_CHANGE_MENU
from bot_tgc.handlers.admin.states import AdminMenu, AddItem, AddCategories, AddAdmin, Mailing, ChangeMenu


def admin_menu_window():
    return Window(
        Const(LEXICON_ADMIN_MENU.get("admin_menu")),
        Group(
            Start(Const(LEXICON_CHANGE_MENU.get("change_menu")), id="change_menu", state=ChangeMenu.main_menu),

            Start(Const(LEXICON_ITEM.get("item_menu")), id="item", state=AddItem.menu),

            Start(Const(LEXICON_CATEGORIES.get("categories_menu")), id="categories",
                  state=AddCategories.categories_menu),

            Start(Const(LEXICON_ADMIN.get("admin_menu")), id="admin", state=AddAdmin.admin_menu),

            Start(Const(LEXICON_MAILING.get("item_menu")), id="mailing", state=Mailing.mailing_menu),

            width=2
        ),
        Url(text=Const("Адм. панель [root:1234]"), url=Const("https://63ce-178-57-114-190.ngrok-free.app/admin/")),
        Cancel(Const(LEXICON_ADMIN_MENU.get("to_menu"))),

        state=AdminMenu.admin_menu
    )

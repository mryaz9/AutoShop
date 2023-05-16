from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const


from handlers.admin.states import AdminMenu, AddItem, AddCategories, AddAdmin, Mailing
from dictionary.dictionary_ru import LEXICON_ADMIN_MENU, LEXICON_ADMIN, LEXICON_CATEGORIES, LEXICON_ITEM, LEXICON_MAILING


def admin_menu_window():
    return Window(
        Const(LEXICON_ADMIN_MENU.get("admin_menu")),

        Start(Const(LEXICON_ITEM.get("item_menu")), id="item", state=AddItem.menu),

        Start(Const(LEXICON_CATEGORIES.get("categories_menu")), id="categories", state=AddCategories.categories_menu),

        Start(Const(LEXICON_ADMIN.get("admin_menu")), id="admin", state=AddAdmin.admin_menu),

        Start(Const(LEXICON_MAILING.get("item_menu")), id="mailing", state=Mailing.mailing_menu),

        Cancel(Const(LEXICON_ADMIN_MENU.get("to_menu"))),

        state=AdminMenu.admin_menu
    )


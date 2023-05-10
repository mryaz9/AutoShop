from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const


from dialogs.admin.states import AdminMenu, AddItem, AddCategories, AddAdmin
from lexicon.lexicon_ru import LEXICON_ADMIN, LEXICON_BUTTON_ADMIN


def admin_menu_window():
    return Window(
        Const(LEXICON_ADMIN["in_admin"]),
        Start(Const(LEXICON_BUTTON_ADMIN["add_assortment"]), id="add_assortment",
              state=AddItem.select_categories),
        Start(Const(LEXICON_BUTTON_ADMIN["add_categories"]), id="add_categories", state=AddCategories.categories_menu),
        Start(Const("Добавить администраторов"), id="add_admin", state=AddAdmin.admin_menu),
        # Start(Const(LEXICON_BUTTON_ADMIN["see_admin"]), id="information", state=Product.show),
        Cancel(Const(LEXICON_BUTTON_ADMIN["exit"])),
        state=AdminMenu.admin_menu
    )

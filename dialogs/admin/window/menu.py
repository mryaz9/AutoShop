from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const


from dialogs.admin.states import AdminMenu, Category
from lexicon.lexicon_ru import LEXICON_ADMIN, LEXICON_BUTTON_ADMIN


def admin_menu_window():
    return Window(
        Const(LEXICON_ADMIN["in_admin"]),
        Start(Const(LEXICON_BUTTON_ADMIN["add_assortment"]), id="add_assortment",
              state=Category.select_categories),
        # Start(Const(LEXICON_BUTTON_ADMIN["show_assortment"]), id="profile", state=BannerSG.default),
        # Start(Const(LEXICON_BUTTON_ADMIN["del_assortment"]), id="️orders", state=Product.show),
        # Start(Const(LEXICON_BUTTON_ADMIN["see_admin"]), id="information", state=Product.show),
        Cancel(Const(LEXICON_BUTTON_ADMIN["exit"])),
        state=AdminMenu.admin_menu
    )

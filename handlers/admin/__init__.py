from aiogram_dialog import Dialog

from dictionary.dictionary_ru import LEXICON_CHANGE_MENU
from handlers.admin import selected, window
from handlers.admin.states import ChangeMenu
from handlers.admin.mailing_menu import window
from handlers.admin.change_menu import window
from handlers.admin.item_menu import window
from handlers.admin.category_menu import window
from handlers.admin.admin_menu import window


def admin_dialogs():
    return [
        Dialog(
            menu.admin_menu_window(),
        ),
        Dialog(
            change_menu.input_photo_window(
                text=LEXICON_CHANGE_MENU.get("main_menu"),
                state=ChangeMenu.main_menu,
                id_input="main_menu"
            ),
            change_menu.input_photo_window(
                text=LEXICON_CHANGE_MENU.get("catalog"),
                state=ChangeMenu.catalog,
                id_input="catalog"
            ),
            change_menu.input_photo_window(
                text=LEXICON_CHANGE_MENU.get("order"),
                state=ChangeMenu.order,
                id_input="order"
            ),
            change_menu.input_photo_window(
                text=LEXICON_CHANGE_MENU.get("profile"),
                state=ChangeMenu.profile,
                id_input="profile"
            ),
            change_menu.input_photo_window(
                text=LEXICON_CHANGE_MENU.get("info"),
                state=ChangeMenu.info,
                id_input="info"
            ),
            change_menu.input_text_window(
                text=LEXICON_CHANGE_MENU.get("info_about"),
                state=ChangeMenu.info_about,
                id_input="info_about"
            ),
            change_menu.confirm_change_menu_window()
        ),
        Dialog(
            add_item.menu_window(),
            add_item.add_files_window(),
            add_item.add_files_confirm_window(),

            add_item.del_item_confirm_window(),

            add_item.categories_window(),
            add_item.subcategories_window(),
            add_item.items_window(),
            add_item.name_window(),
            add_item.amount_window(),
            add_item.photo_window(),
            add_item.price_window(),
            add_item.description_window(),
            add_item.confirm_window(),
        ),
        Dialog(
            add_categories.menu_window(),

            add_categories.select_categories_window(),
            add_categories.select_subcategories_window(),

            add_categories.input_name_category_window(),
            add_categories.photo_categories_window(),
            add_categories.add_categories_confirm_window(),

            add_categories.del_categories_confirm_window(),

            add_categories.input_name_subcategory_window(),
            add_categories.photo_subcategories_window(),
            add_categories.add_subcategories_confirm_window(),

            add_categories.del_subcategories_confirm_window()
        ),
        Dialog(
            add_admin.menu_window(),
            add_admin.add_admin_window(),
            add_admin.view_admin_window(),
        ),
        Dialog(
            mailing.menu_window(),
            mailing.create_mailing_window(),
        )
    ]

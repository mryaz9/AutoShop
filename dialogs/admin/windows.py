from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button
from aiogram_dialog.widgets.text import Const, Format

from dialogs.admin import selected, keyboard, states, getters
from dialogs.admin.states import AdminMenu, AddAssortiment

from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_BUTTON_ADMIN, LEXICON_ADMIN, LEXICON_FSM_SHOP, LEXICON_MAIN


def admin_menu_window():
    return Window(
        Const(LEXICON_ADMIN["in_admin"]),
        Start(Const(LEXICON_BUTTON_ADMIN["add_assortment"]), id="add_assortment",
              state=AddAssortiment.select_categories),
        # Start(Const(LEXICON_BUTTON_ADMIN["show_assortment"]), id="profile", state=BannerSG.default),
        # Start(Const(LEXICON_BUTTON_ADMIN["del_assortment"]), id="️orders", state=Product.show),
        # Start(Const(LEXICON_BUTTON_ADMIN["see_admin"]), id="information", state=Product.show),
        Cancel(Const(LEXICON_BUTTON_ADMIN["exit"])),
        state=AdminMenu.admin_menu
    )


def categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboard.paginated_categories(selected.on_chosen_category),
        Button(Const(
            LEXICON_FSM_SHOP["add_new_category"]), id="add_new_category", on_click=selected.on_add_new_category
        ),
        Cancel(Const(LEXICON_MAIN["back"])),
        state=states.AddAssortiment.select_categories,
        getter=getters.get_categories
    )


def subcategories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["subcategory"]),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        Button(Const(
            LEXICON_FSM_SHOP["add_new_category"]), id="add_new_subcategory", on_click=selected.on_add_new_category
        ),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.select_subcategories,
        getter=getters.get_subcategories
    )


def add_categories_code_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_category_code"]),
        MessageInput(selected.on_add_new_category_code, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.add_new_categories_code,
    )


def add_categories_name_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_category_name"]),
        MessageInput(selected.on_add_new_category_name, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.add_new_categories_name,
    )


def add_subcategories_code_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_subcategory_code"]),
        MessageInput(selected.on_add_new_subcategory_code, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.add_new_subcategories_code,
    )


def add_subcategories_name_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_subcategory_name"]),
        MessageInput(selected.on_add_new_subcategory_name, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.add_new_subcategories_name,
    )


def name_window():
    return Window(
        Const(LEXICON_FSM_SHOP["name"]),
        MessageInput(selected.on_chosen_name, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.name,
    )


def amount_window():
    return Window(
        Const(LEXICON_FSM_SHOP["amount"]),
        MessageInput(selected.on_chosen_amount, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.amount,
    )


def photo_window():
    return Window(
        Const(LEXICON_FSM_SHOP["photo"]),
        MessageInput(selected.on_chosen_photo, ContentType.PHOTO),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.photo,
    )


def price_window():
    return Window(
        Const(LEXICON_FSM_SHOP["price"]),
        MessageInput(selected.on_chosen_price, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.price,
    )


def time_action_window():
    return Window(
        Const(LEXICON_FSM_SHOP["time_action"]),
        MessageInput(selected.on_chosen_time_action, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.time_action,
    )


def description_window():
    return Window(
        Const(LEXICON_FSM_SHOP["description"]),
        MessageInput(selected.on_chosen_description, ContentType.TEXT),
        Back(Const(LEXICON_MAIN["back"])),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.description,
    )


def confirm_window():
    return Window(
        Const("Все правильно?"),
        Format(LEXICON_FSM_SHOP["done_2"]),
        keyboard.confirm_kb(selected.on_chosen_confirm),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddAssortiment.confirm,
        getter=getters.get_confirm_add
    )

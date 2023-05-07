from aiogram_dialog import Window, Data, DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Back, Button, Row, SwitchTo, Start
from aiogram_dialog.widgets.text import Const, Format

from dialogs.assortiment import selected, states
from dialogs import getters, keyboard
from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_MAIN


def categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboard.paginated_categories(selected.on_chosen_category),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.Assortment.select_categories,
        getter=getters.get_categories
    )


def subcategories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["subcategory"]),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.Assortment.select_subcategories,
        getter=getters.get_subcategories
    )


def product_window():
    return Window(
        Const(LEXICON_INLINE_MENU["name"]),
        keyboard.paginated_product(selected.on_chosen_products),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.Assortment.select_product,
        getter=getters.get_product
    )


def product_info_window():
    return Window(
        Format(LEXICON_INLINE_MENU["item"]),
        Button(
            Const(LEXICON_MAIN["buy"]),
            id="buy_product",
            on_click=selected.on_chosen_product_info,
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.Assortment.select_product_info,
        getter=getters.get_product_info
    )


def buy_product_window():
    return Window(
        Format("Для {product}\nИмеется {amount}шт.\nСколько вы хотите купить?"),
        TextInput(
            id="enter_amount",
            on_success=selected.on_entered_amount,
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.BuyProduct.enter_amount,
        getter=getters.get_buy_product

    )


def confirm_buy_window():
    return Window(
        Format("Вы хотите купить {product} {amount_user} шт\nЗа {total_amount}руб.\nВы уверены?"),
        Button(Const("Да"),
               id="confirm_buy",
               on_click=selected.on_confirm_buy),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),

        state=states.BuyProduct.confirm,
        getter=getters.get_buy_product
    )

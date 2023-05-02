from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Back, Button
from aiogram_dialog.widgets.text import Const, Format

from dialogs.bot_main_menu import keyboards, selected, states, getters
from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_MAIN


def categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboards.paginated_categories(selected.on_chosen_category),
        Cancel(Const(LEXICON_MAIN["back"])),
        state=states.BotMenu.select_categories,
        getter=getters.get_categories
    )


def subcategories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["subcategory"]),
        keyboards.paginated_subcategories(selected.on_chosen_subcategories),
        Cancel(Const(LEXICON_MAIN["back"])),
        state=states.BotMenu.select_subcategories,
        getter=getters.get_subcategories
    )


def product_window():
    return Window(
        Const(LEXICON_INLINE_MENU["name"]),
        keyboards.paginated_product(selected.on_chosen_product),
        Back(Const(LEXICON_MAIN["back"])),
        state=states.BotMenu.select_product,
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
        Back(Const(LEXICON_MAIN["back"])),
        state=states.BotMenu.select_product_info,
        getter=getters.get_product_info
    )

def buy_product_window():
    return Window(
        Format("""
        {product.name}\n
        {product.count}
        """
        ),
        TextInput(
            id="enter_amount",
            on_success=selected.on_entered_amount,
        ),
        Cancel(Const(LEXICON_MAIN["back"])),
        Cancel(Const("Выбрать другой продукт"), id="cancel_sw_to_select", result={"switch_to": "select_products"}),
        state=states.BuyProduct.enter_amount,
        getter=getters.get_product

    )
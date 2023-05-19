from typing import Dict

from aiogram_dialog import Window, Data, DialogManager
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Back, Button, Row
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from handlers import getters, keyboard
from handlers.users.assortiment import selected, states
from dictionary.dictionary_ru import LEXICON_ASSORTIMENT


def categories_window():
    return Window(
        DynamicMedia("photo"),
        Const(LEXICON_ASSORTIMENT.get("categories")),
        keyboard.paginated_categories(selected.on_chosen_category),
        state=states.BotMenu.select_categories,
        getter=getters.getter_category
    )


def subcategories_window():
    return Window(
        DynamicMedia("photo"),
        Const(LEXICON_ASSORTIMENT.get("subcategories")),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        state=states.BotMenu.select_subcategories,
        getter=getters.getter_subcategory
    )


def product_window():
    return Window(
        DynamicMedia("photo"),
        Const(LEXICON_ASSORTIMENT.get("items")),
        keyboard.paginated_product(selected.on_chosen_product),
        state=states.BotMenu.select_product,
        getter=getters.getter_product
    )


def product_info_window():
    return Window(
        DynamicMedia("photo"),
        Format(LEXICON_ASSORTIMENT.get("card")),
        Button(
            Const(LEXICON_ASSORTIMENT.get("buy_product")),
            id="buy_product",
            on_click=selected.on_chosen_product_info,
        ),
        Row(
            Cancel(Const(LEXICON_ASSORTIMENT.get("to_menu"))),
            Back(Const(LEXICON_ASSORTIMENT.get("back_select_items"))),
        ),
        state=states.BotMenu.select_product_info,
        getter=getters.getter_product_info
    )


def buy_product_window():
    return Window(
        DynamicMedia("photo"),
        Format(LEXICON_ASSORTIMENT.get("buy_product_window")),
        Format(LEXICON_ASSORTIMENT.get("buy_product_amount")),

        TextInput(
            id="enter_amount",
            on_success=selected.on_entered_amount,
        ),
        Row(
            Cancel(Const(LEXICON_ASSORTIMENT.get("back_items_info"))),
            Cancel(Const(LEXICON_ASSORTIMENT.get("back_items_names")), id="cancel_sw_to_select",
                   result={"switch_to_window": "select_products"}),
        ),
        state=states.BuyProduct.enter_amount,
        getter=getters.getter_buy_product
    )


def confirm_buy_window():
    return Window(
        DynamicMedia("photo"),
        Format(LEXICON_ASSORTIMENT.get("accept_buy_item_amount")),
        Format(LEXICON_ASSORTIMENT.get("accept_buy_item")),

        Button(Const(LEXICON_ASSORTIMENT.get("confirm_buy")),
               id="confirm_buy",
               on_click=selected.on_confirm_buy),
        Row(
            Cancel(Const(LEXICON_ASSORTIMENT.get("back_items_amount"))),
            Cancel(Const(LEXICON_ASSORTIMENT.get("back_items_names")),
                   id="cancel_sw_to_select",
                   result={"switch_to_window": "select_products"}),
        ),
        state=states.BuyProduct.confirm,
        getter=getters.getter_buy_product
    )


async def on_process_result(data: Data, result: dict, manager: DialogManager, **kwargs):
    if result:
        switch_to_window = result.get("switch_to_window")
        if switch_to_window == "select_products":
            await manager.switch_to(state=states.BotMenu.select_product)

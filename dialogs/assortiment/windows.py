from aiogram_dialog import Window, Data, DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Back, Button, Column, Row
from aiogram_dialog.widgets.text import Const, Format

from dialogs.assortiment import keyboard, selected, states, getters
from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_MAIN


def categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboard.paginated_categories(selected.on_chosen_category),
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.BotMenu.select_categories,
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
        state=states.BotMenu.select_subcategories,
        getter=getters.get_subcategories
    )


def product_window():
    return Window(
        Const(LEXICON_INLINE_MENU["name"]),
        keyboard.paginated_product(selected.on_chosen_product),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
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
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.BotMenu.select_product_info,
        getter=getters.get_product_info
    )


def buy_product_window():
    return Window(
        Format("Для {product}\nИмеется {amount}шт.\nСколько вы хотите купить?"),
        TextInput(
            id="enter_amount",
            on_success=selected.on_entered_amount,
        ),
        Cancel(Const(LEXICON_MAIN["back"])),
        Cancel(Const("Выбрать другой продукт"), id="cancel_sw_to_select", result={"switch_to_window": "select_products"}),
        state=states.BuyProduct.enter_amount,
        getter=getters.get_buy_product

    )


def confirm_buy_window():
    return Window(
        Format("Вы хотите купить {product} {amount_user} шт\nЗа {total_amount}руб.\nВы уверены?"),
        Button(Const("Да"),
               id="confirm_buy",
               on_click=selected.on_confirm_buy),
        Back(Const("Изменить кол-во")),
        Cancel(Const("Выбрать другой продукт"),
               id="cancel_sw_to_select",
               result={"switch_to_window": "select_products"}),

        state=states.BuyProduct.confirm,
        getter=getters.get_buy_product
    )


async def on_process_result(data: Data, result: dict, manager: DialogManager, **kwargs):
    if result:
        switch_to_window = result.get("switch_to_window")
        if switch_to_window == "select_products":
            await manager.switch_to(state=states.BotMenu.select_product)
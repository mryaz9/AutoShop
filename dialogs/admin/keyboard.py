import operator
from typing import Dict

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import DialogUpdateEvent
from aiogram_dialog.widgets.common import Whenable, ManagedWidget
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Row, Button, Back, ListGroup, Checkbox, \
    ManagedCheckboxAdapter, Radio, Group, SwitchTo
from aiogram_dialog.widgets.text import Format, Const

from dialogs.admin import states
from lexicon.lexicon_ru import LEXICON_MAIN, LEXICON_BUTTON_ADMIN, LEXICON_FSM_SHOP

SCROLLING_HEIGHT = 6
SCROLLING_WIDTH = 1


def when_checked(data: Dict, checkbox: Whenable, manager: DialogManager) -> bool:
    check: ManagedCheckboxAdapter = manager.find("check")
    return check.is_checked()


def paginated_categories(on_click):
    return Group(
        ScrollingGroup(
            ListGroup(
                Checkbox(
                    Format("✓ {item[0]}"),
                    Format("  {item[0]}"),
                    id="check"
                ),
                Row(
                    SwitchTo(Format(
                        "{item[0]}"), id="add_new_category",
                        state=states.Category.add_categories,
                    ),
                    SwitchTo(Const(
                        LEXICON_BUTTON_ADMIN["hide"]), id="add_new_category",
                        state=states.Category.hide_categories
                    ),
                    SwitchTo(Const(
                        LEXICON_BUTTON_ADMIN["edit"]), id="add_new_category",
                        state=states.Category.edit_categories
                    ),
                    SwitchTo(Const(
                        LEXICON_BUTTON_ADMIN["del"]), id="add_new_category",
                        state=states.Category.add_categories
                    ),
                    when=when_checked,
                ),
                id="lg",
                item_id_getter=operator.itemgetter(1),
                items="categories",

            ),
            id="categories_id",
            height=SCROLLING_HEIGHT,
        ),
    )


def paginated_subcategories(on_click):
    return ScrollingGroup(ListGroup(
        Checkbox(
            Format("✓ {item[0]}"),
            Format("  {item[0]}"),
            id="check",
        ),
        Row(
            Select(
                Format("{item}"),
                id="select",
                item_id_getter=str,
                items=[LEXICON_BUTTON_ADMIN["select"], LEXICON_BUTTON_ADMIN["hide"],
                       LEXICON_BUTTON_ADMIN["edit"], LEXICON_BUTTON_ADMIN["del"]],

                when=when_checked,
                on_click=on_click
            )
        ),
        id="lg",
        item_id_getter=operator.itemgetter(1),
        items="subcategories",

    ),
        id="subcategories_id",
        height=SCROLLING_HEIGHT,
    )


def paginated_product(on_click):
    return ScrollingGroup(ListGroup(
        Checkbox(
            Format("✓ {item[0]}"),
            Format("  {item[0]}"),
            id="check",
        ),
        Row(
            Select(
                Format("{item}"),
                id="select",
                item_id_getter=str,
                items=[LEXICON_BUTTON_ADMIN["select"], LEXICON_BUTTON_ADMIN["hide"],
                       LEXICON_BUTTON_ADMIN["edit"], LEXICON_BUTTON_ADMIN["del"]],

                when=when_checked,
                on_click=on_click
            )
        ),
        id="lg",
        item_id_getter=operator.itemgetter(1),
        items="product",

    ),
        id="product_id",
        height=SCROLLING_HEIGHT,
    )


def confirm_kb(on_click):
    return Row(
        Button(
            Const("Да"),
            id="confirm_yes",
            on_click=on_click
        ),
        Back(Const(LEXICON_MAIN["back"])),
    )

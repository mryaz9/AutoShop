import operator

from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Row, Button, Back, Group, PrevPage, NextPage, Cancel
from aiogram_dialog.widgets.text import Format, Const, Multi

from lexicon.lexicon_ru import LEXICON_MAIN

SCROLLING_HEIGHT = 6
SCROLLING_WIDTH = 1


def paginated_categories(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Format('{item[0]}'),
                id="s_scroll_categories",
                item_id_getter=operator.itemgetter(1),
                items="categories",
                on_click=on_click
            ),
            hide_pager=True,
            id="categories_id",
            width=SCROLLING_WIDTH,
            height=SCROLLING_HEIGHT,
        ),
        Row(
            PrevPage(
                scroll="categories_id", text=Format("◀️"),
            ),
            NextPage(
                scroll="categories_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"]))
        ),
    )


def paginated_subcategories(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Format('{item[0]}'),
                id="s_scroll_subcategories",
                item_id_getter=operator.itemgetter(1),
                items="subcategories",
                on_click=on_click
            ),
            hide_pager=True,
            id="subcategories_id",
            width=SCROLLING_WIDTH,
            height=SCROLLING_HEIGHT,
        ),
        Row(
            PrevPage(
                scroll="subcategories_id", text=Format("◀️"),
            ),
            NextPage(
                scroll="subcategories_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
    )


def paginated_product(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Multi(
                    Format("{item[0].name}"),
                    Format("{item[0].price}руб."),
                    sep="\n",
                ),
                id="s_scroll_product",
                item_id_getter=operator.itemgetter(1),
                items="product",
                on_click=on_click
            ),
            hide_pager=True,
            id="product_id",
            width=SCROLLING_WIDTH,
            height=SCROLLING_HEIGHT,
        ),
        Row(
            PrevPage(
                scroll="product_id", text=Format("◀️"),
            ),
            NextPage(
                scroll="product_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
    )


def paginated_orders(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Format('{item[0].name} {item[1]}'),
                id="s_scroll_orders",
                item_id_getter=operator.itemgetter(1),
                items="orders",
                on_click=on_click
            ),
            hide_pager=True,
            id="orders_id",
            width=SCROLLING_WIDTH,
            height=SCROLLING_HEIGHT,
        ),
        Row(
            PrevPage(
                scroll="orders_id", text=Format("◀️"),
            ),
            NextPage(
                scroll="orders_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
        ),
    )


def confirm_kb(on_click):
    return Row(
        Button(
            Const("Да"),
            id="confirm_yes",
            on_click=on_click
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
    )

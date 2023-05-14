import operator

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Row, Button, Back, Group, PrevPage, NextPage, Cancel, \
    CurrentPage
from aiogram_dialog.widgets.text import Format, Const, Multi
from magic_filter import F

from lexicon.lexicon_ru import LEXICON_MAIN, LEXICON_ASSORTIMENT

SCROLLING_HEIGHT = 6
SCROLLING_WIDTH = 1


def paginated_categories(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Format(
                    '{item[0]}',
                    #when=is_show
                    ),
                id="s_scroll_categories",
                item_id_getter=operator.itemgetter(1),
                items="categories",
                on_click=on_click,
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
            CurrentPage(
                scroll="categories_id", text=Format("{current_page1}"),
            ),
            NextPage(
                scroll="categories_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_ASSORTIMENT.get("to_menu")))
        ),
    )


def paginated_subcategories(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Format(
                    '{item[0]}',
                    #when=is_show
                       ),
                id="s_scroll_subcategories",
                item_id_getter=operator.itemgetter(1),
                items="subcategories",
                on_click=on_click,
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
            CurrentPage(
                scroll="subcategories_id", text=Format("{current_page1}"),
            ),
            NextPage(
                scroll="subcategories_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_ASSORTIMENT.get("to_menu"))),
            Back(Const(LEXICON_ASSORTIMENT.get("back_select_categories"))),
        ),
    )


def paginated_product(on_click, show=None, hide=lambda d, w, m: False):
    return Group(
        ScrollingGroup(
            Select(
                Multi(
                    Format("{item[0].name}"),
                    Format("{item[0].price}руб."),
                    Format("{item[0].show}", when=hide),

                    sep="\n",
                    when=show
                ),

                id="s_scroll_product",
                item_id_getter=operator.itemgetter(1),
                items="product",
                on_click=on_click,
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
            CurrentPage(
                scroll="product_id", text=Format("{current_page1}"),
            ),
            NextPage(
                scroll="product_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_ASSORTIMENT.get("to_menu"))),
            Back(Const(LEXICON_ASSORTIMENT.get("back_select_subcategories"))),
        ),
    )


def is_show(dict_when: dict, when: Whenable, dialog_manager: DialogManager) -> bool:
    items = dict_when.get("item")
    return items[0].show


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
            CurrentPage(
                scroll="orders_id", text=Format("{current_page1}"),
            ),
            NextPage(
                scroll="orders_id", text=Format("▶️"),
            ),
        ),
        Row(
            Cancel(Const(LEXICON_ASSORTIMENT.get("to_menu"))),
        ),
    )

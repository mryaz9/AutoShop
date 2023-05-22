import operator

from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Row, Back, Group, PrevPage, NextPage, Cancel, \
    CurrentPage
from aiogram_dialog.widgets.text import Format, Const, Multi

from dictionary.dictionary_ru import LEXICON_ASSORTIMENT

SCROLLING_HEIGHT = 6
SCROLLING_WIDTH = 1


def paginated_categories(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Format(
                    '{item[0].title}'
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
                    '{item[0].title}'
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


def paginated_product(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Multi(
                    Format("{item[0].title} | "),
                    Format("{item[0].price}руб."),
                    sep="\n",
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


def paginated_admins(on_click):
    return Group(
        ScrollingGroup(
            Select(
                Format(
                    '{item[0].id}'
                ),
                id="s_scroll_admins",
                item_id_getter=operator.itemgetter(1),
                items="admins",
                on_click=on_click,
            ),
            hide_pager=True,
            id="admins_id",
            width=SCROLLING_WIDTH,
            height=SCROLLING_HEIGHT,
        ),
        Row(
            PrevPage(
                scroll="admins_id", text=Format("◀️"),
            ),
            CurrentPage(
                scroll="admins_id", text=Format("{current_page1}"),
            ),
            NextPage(
                scroll="admins_id", text=Format("▶️"),
            ),
        ),
    )

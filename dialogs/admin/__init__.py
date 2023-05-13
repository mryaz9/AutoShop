from aiogram_dialog import Dialog

from dialogs.admin.window import menu, add_product, add_categories, add_admin, mailing


def admin_dialogs():
    return [
        Dialog(
            menu.admin_menu_window(),
        ),
        Dialog(
            add_product.menu_window(),
            add_product.hide_item_window(),

            add_product.categories_window(),
            add_product.subcategories_window(),
            add_product.name_window(),
            add_product.amount_window(),
            add_product.photo_window(),
            add_product.price_window(),
            add_product.time_action_window(),
            add_product.description_window(),
            add_product.confirm_window(),
        ),
        Dialog(
            add_categories.menu_window(),
            add_categories.select_categories_window(),
            add_categories.add_categories_window(),
            add_categories.add_subcategories_window(),
        ),
        Dialog(
            add_admin.menu_window(),
            add_admin.add_admin_window(),
        ),
        Dialog(
            mailing.menu_window(),
            mailing.create_mailing_window(),
        )
    ]

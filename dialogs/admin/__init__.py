from aiogram_dialog import Dialog

from dialogs.admin.window import menu, add_admin, categories, subcategories, product, add_product


def admin_dialogs():
    return [
        Dialog(
            menu.admin_menu_window(),
        ),
        #Dialog(
        #    add_admin.see_admin(),
        #    add_admin.add_admin(),
        #    add_admin.del_admin(),
        #),
        Dialog(
            categories.categories_window(),
        #    categories.hide_categories_window(),
            categories.add_categories_window(),
        #    categories.del_categories_window(),
        ),
        Dialog(
            subcategories.subcategories_window(),
        #    subcategories.hide_subcategories_window(),
        #    subcategories.add_subcategories_window(),
        #    subcategories.del_subcategories_window(),
        ),
        Dialog(
            product.product_window(),
        #    product.hide_product_window(),
        #    product.add_product_window(),
        #    product.del_product_window(),
        ),
        Dialog(
            add_product.name_window(),
            add_product.amount_window(),
            add_product.files_window(),
            add_product.photo_window(),
            add_product.price_window(),
            add_product.time_action_window(),
            add_product.description_window(),
            add_product.confirm_window(),
        )
    ]

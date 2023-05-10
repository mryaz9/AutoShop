from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Row, Back, Select
from aiogram_dialog.widgets.text import Const, Multi, Format

from dialogs.getters import get_profile, get_order
from dialogs.keyboard import paginated_orders
from dialogs.profile.states import Profile, Purchases
from lexicon.lexicon_ru import LEXICON_MAIN


def profile_window():
    return Window(
        Multi(
            Const("📱 Ваш профиль:"),
            Const("➖➖➖➖➖➖➖➖➖➖➖➖➖"),
            Format("🔑 Мой ID: {user_id}"),
            Format("Full Name: {full_name}"),
            Format("👤 Логин: {username}"),
            Format("💳 Баланс: {balance}руб."),
            Format("🕜 Регистрация: {register_time}"),
            sep="\n"
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
        ),
        state=Profile.profile,
        getter=get_profile
    )


def orders_window():
    return Window(
        Const("Заказы:"),
        paginated_orders(on_click=None),  # Todo: Добавить поддержку нажатия на кнопку
        state=Purchases.purchases,
        getter=get_order
    )

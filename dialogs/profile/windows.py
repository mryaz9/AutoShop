from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Row, Start
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Multi, Format

from dialogs import keyboard
from dialogs.getters import get_profile, get_orders
from dialogs.keyboard import paginated_orders
from dialogs.profile.states import Profile, Purchases
from lexicon.lexicon_ru import LEXICON_MAIN, LEXICON_PROFILE
from payment.states import Payment


def profile_window():
    return Window(
        StaticMedia(
            path="/home/mryaz/Рабочий стол/Tg_Bot_tgc/sourse/profile.jpg",
        ),
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
        Start(
            Const("Пополнить баланс"),
            id="up_balance",
            state=Payment.payment_select
        ),
        Row(
            Cancel(Const(LEXICON_PROFILE.get("to_menu"))),
        ),
        state=Profile.profile,
        getter=get_profile
    )


def orders_window():
    return Window(
        StaticMedia(
            path="/home/mryaz/Рабочий стол/Tg_Bot_tgc/sourse/order.jpg",
        ),
        Const("Заказы:"),
        paginated_orders(on_click=None),  # Todo: Добавить поддержку нажатия на кнопку
        state=Purchases.purchases,
        getter=get_orders
    )


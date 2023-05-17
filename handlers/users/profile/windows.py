from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Row, Start
from aiogram_dialog.widgets.text import Const, Multi, Format

from handlers.getters import getter_profile, getter_orders
from handlers.keyboard import paginated_orders
from handlers.users.profile.states import Profile, Purchases
from dictionary.dictionary_ru import LEXICON_PROFILE
from payment.states import Payment


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
        Start(
            Const("Пополнить баланс"),
            id="up_balance",
            state=Payment.payment_select
        ),
        Row(
            Cancel(Const(LEXICON_PROFILE.get("to_menu"))),
        ),
        state=Profile.profile,
        getter=getter_profile
    )


def orders_window():
    return Window(
        Const("Заказы:"),
        paginated_orders(on_click=None),  # Todo: Добавить поддержку нажатия на кнопку
        state=Purchases.purchases,
        getter=getter_orders
    )


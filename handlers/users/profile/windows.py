from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Row, Start
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Multi, Format

from dictionary.dictionary_ru import LEXICON_PROFILE
from handlers.getters import getter_profile
from handlers.users.profile.states import Profile
from handlers.payment.states import Payment


def profile_window():
    return Window(
        DynamicMedia("photo"),
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

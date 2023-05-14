from aiogram_dialog import Dialog
from glQiwiApi import QiwiP2PClient

from config.config import Config, load_config
from payment import windows


def payment_dialogs():
    return [
        Dialog(
            windows.payment_select_window(),
            windows.input_amount_window(),
            windows.payment_qiwi_window(),
            windows.payment_crypto_window(),
            windows.select_assets_window(),
            #windows.payment_admin_window(),
        )
    ]

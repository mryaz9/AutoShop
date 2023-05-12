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
        )
    ]


def init_qiwi_client():
    config: Config = load_config()

    p2p = QiwiP2PClient(secret_p2p=config.tg_bot.qiwi_token,
                        shim_server_url="http://referrerproxy-env.eba-cxcmwwm7.us-east-1.elasticbeanstalk.com/proxy/p2p/")

    return p2p

from datetime import datetime, timedelta

from aiogram_dialog import DialogManager
from glQiwiApi import QiwiP2PClient
from loguru import logger

from config.config import load_config, Config
from payment import init_qiwi_client


async def get_payment_qiwi(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    amount = ctx.dialog_data.get("amount")

    p2p = init_qiwi_client()

    bill = await p2p.create_p2p_bill(amount=float(amount), expire_at=datetime.now() + timedelta(minutes=30),
                                     pay_source_filter=["qw", "card", "mobile"])

    await p2p.close()
    data = {
        "amount": amount,
        "bill_id": bill.id,
        "bill_url": bill.pay_url
    }
    return data

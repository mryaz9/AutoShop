from datetime import datetime, timedelta
from aiocryptopay.const import Assets

from aiogram_dialog import DialogManager
from utils.init_payment import init_qiwi_client, init_crypto_client


async def get_payment_qiwi(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    amount = ctx.dialog_data.get("amount")

    p2p = init_qiwi_client()

    bill = await p2p.create_p2p_bill(amount=float(amount), expire_at=datetime.now() + timedelta(minutes=30),
                                     pay_source_filter=["qw", "card", "mobile"])

    ctx.dialog_data.update(bill_id=bill.id)
    await p2p.close()
    data = {
        "amount": amount,
        "bill_id": bill.id,
        "bill_url": bill.pay_url
    }
    return data


async def get_assets_crypto(dialog_manager: DialogManager, **kwargs):
    data = {
        "assets": [(values, values)
                   for values in Assets.values()
                   ]
    }
    return data


async def get_payment_crypto(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    amount = ctx.dialog_data.get("amount")
    asset = ctx.dialog_data.get("asset")

    crypto = init_crypto_client()
    rates = await crypto.get_exchange_rates()
    for rate in rates:
        if rate.source == asset and rate.target == "RUB":
            amount /= rate.rate

    invoice = await crypto.create_invoice(asset=asset, amount=amount)

    ctx.dialog_data.update(bill_id=invoice.invoice_id)

    crypto.close()

    data = {
        "amount": amount,
        "asset": asset,
        "bill_id": invoice.invoice_id,
        "bill_url": invoice.pay_url
    }
    return data

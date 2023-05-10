import asyncio

from aiocryptopay import AioCryptoPay, Networks

crypto = AioCryptoPay(token='7292:AAL8Bc3yQnjNOVkZqDNsJ3nMLUguhFrYjYb', network=Networks.TEST_NET)


async def create_payment_crypto_bot(asset, amount):
    invoice = await crypto.create_invoice(asset=asset, amount=amount)
    return invoice


async def check_payment_crypto_bot(invoice):
    status = await crypto.get_invoices(invoice_ids=invoice.invoice_id)
    return status

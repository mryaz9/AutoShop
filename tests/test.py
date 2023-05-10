import asyncio

from aiocryptopay import AioCryptoPay, Networks


async def test():
    crypto = AioCryptoPay(token='7292:AAL8Bc3yQnjNOVkZqDNsJ3nMLUguhFrYjYb', network=Networks.TEST_NET)
    invoice = await crypto.create_invoice(asset='TON', amount=1.5)
    return invoice

    invoices = await crypto.get_invoices(invoice_ids=invoice.invoice_id)
    print(invoices.status)

asyncio.run(test())

from database.init_database import db
from database.models import Purchases


async def add_purchases(purchases: Purchases):
    new_purchases = await purchases.create()
    return new_purchases


async def get_purchases(buyer_id) -> list[Purchases]:
    purchases = await Purchases.query.where(
        Purchases.buyer_id == buyer_id
    ).gino.all()
    return purchases

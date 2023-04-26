from database.init_database import db
from database.models import Purchases


async def add_purchases(**kwargs):
    new_purchases = await Purchases(**kwargs).create()
    return new_purchases



from database.command.database_admin import get_all_admin
from lexicon.lexicon_ru import LEXICON_ADMIN_INFO


async def startup(bot):
    for admin in await get_all_admin():
        await bot.send_message(chat_id=int(admin.user_id), text=LEXICON_ADMIN_INFO["startup"])


async def shutdown(bot):
    for admin in await get_all_admin():
        await bot.send_message(chat_id=int(admin.user_id), text=LEXICON_ADMIN_INFO["shutdown"])

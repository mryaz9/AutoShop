from aiogram import Router, types

router = Router()


@router.errors()
async def errors_handler(update: types.Update, exception: Exception):
    await update.message.answer(f'Произошла ошибка: {exception}')

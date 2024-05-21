from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()


@router.message(Command('help'))
async def bot_help(message: types.Message):
    text = ("Commands:",
            "/start - Start the bot conversation",
            "/help - Get help",)
    await message.answer(text="\n".join(text))

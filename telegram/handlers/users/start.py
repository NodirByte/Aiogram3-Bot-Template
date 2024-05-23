from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\!",
                         parse_mode=ParseMode.MARKDOWN_V2)
